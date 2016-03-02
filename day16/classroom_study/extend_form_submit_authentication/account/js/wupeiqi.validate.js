/*
<input type="text" name="name" id="id1" data-val="true" data-val-required="请输入Id。" />
<span class="field-validation-valid" data-valmsg-for="name" data-valmsg-replace="true"></span>
*/
(function ($) {
    var $jQval = $.validator,
        data_validation = "WuPeiqiValidate";

    function setValidationValues(options, ruleName, value) {
        options.rules[ruleName] = value;
        if (options.message) {
            options.messages[ruleName] = options.message;
        }
    }

    function escapeAttributeValue(value) {
        // As mentioned on http://api.jquery.com/category/selectors/
        return value.replace(/([!"#$%&'()*+,./:;<=>?@\[\\\]^`{|}~])/g, "\\$1");
    }

    function getModelPrefix(fieldName) {
        return fieldName.substr(0, fieldName.lastIndexOf(".") + 1);
    }

    function appendModelPrefix(value, prefix) {
        if (value.indexOf("*.") === 0) {
            value = value.replace("*.", prefix);
        }
        return value;
    }

    function onError(error, inputElement) {  // 'this' is the form element
        var container = $(this).find("[data-valmsg-for='" + escapeAttributeValue(inputElement[0].name) + "']"),
            replaceAttrValue = container.attr("data-valmsg-replace"),
            replace = replaceAttrValue ? $.parseJSON(replaceAttrValue) !== false : null;

        container.removeClass("field-validation-valid").addClass("field-validation-error");
        error.data("unobtrusiveContainer", container);

        if (replace) {
            container.empty();
            error.removeClass("input-validation-error").appendTo(container);
        }
        else {
            error.hide();
        }
    }

    function onErrors(event, validator) {  // 'this' is the form element
        var container = $(this).find("[data-valmsg-summary=true]"),
            list = container.find("ul");

        if (list && list.length && validator.errorList.length) {
            list.empty();
            container.addClass("validation-summary-errors").removeClass("validation-summary-valid");

            $.each(validator.errorList, function () {
                $("<li />").html(this.message).appendTo(list);
            });
        }
    }

    function onSuccess(error) {  // 'this' is the form element
        var container = error.data("unobtrusiveContainer"),
            replaceAttrValue = container.attr("data-valmsg-replace"),
            replace = replaceAttrValue ? $.parseJSON(replaceAttrValue) : null;

        if (container) {
            container.addClass("field-validation-valid").removeClass("field-validation-error");
            error.removeData("unobtrusiveContainer");

            if (replace) {
                container.empty();
            }
        }
    }

    function onReset(event) {  // 'this' is the form element
        var $form = $(this);
        $form.data("validator").resetForm();
        $form.find(".validation-summary-errors")
            .addClass("validation-summary-valid")
            .removeClass("validation-summary-errors");
        $form.find(".field-validation-error")
            .addClass("field-validation-valid")
            .removeClass("field-validation-error")
            .removeData("unobtrusiveContainer")
            .find(">*")  // If we were using valmsg-replace, get the underlying error
                .removeData("unobtrusiveContainer");
    }


    //为每个form配置jquery.validate信息，并返回配置信息集合
    function validationInfo(form) {
        var $form = $(form),//选中的form
            result = $form.data(data_validation),//在form元素上获取数据（validate配置集合，），并返回jquery对象
            onResetProxy = $.proxy(onReset, form);//重置form，将错误提示信息移除
        
        if (!result) {

            result = {
                options: {  // options structure passed to jQuery Validate's validate() method
                    errorClass: "input-validation-error",//错误css
                    errorElement: "span",//错误标签
                    errorPlacement: $.proxy(onError, form),//在此form内执行onError方法
                    invalidHandler: $.proxy(onErrors, form),
                    messages: {},
                    rules: {},
                    success: $.proxy(onSuccess, form)
                },
                attachValidation: function () {
                    $form
                        .unbind("reset." + data_validation, onResetProxy)//删除绑定的reset.WuPeiqiValidate事件
                        .bind("reset." + data_validation, onResetProxy)//再绑定reset.WuPeiqiValidate事件，事件触发时，执行$.proxy(onReset, form)，即：执行form上下文中的onReset方法
                        .validate(this.options);//绑定事件和方法，并执行validate方法将form进行验证
                },
                validate: function () {  // a validation function that is called by unobtrusive Ajax--暂时不晓得用法
                    $form.validate();
                    return $form.valid();
                }
            };
            $form.data(data_validation, result);//以key-value的形式保存在form元素上
        }
        return result;
    }


    $jQval.WuPeiqi = {
        adapters: [],

        //element表示每个属性 data-val等于true的标签
        parseElement: function (element, skipAttach) {

            var $element = $(element),//属性 data-val等于true的标签
                form = $element.parents("form")[0],//获取当前标签的form
                valInfo, rules, messages;

            if (!form) {  // Cannot do client-side validation without a form
                return;//如果标签不在form中，则退出
            }
            valInfo = validationInfo(form);//获取在parse方法中为每个form设置的配置集合（$form.data保存在form中的数据）
            valInfo.options.rules[element.name] = rules = {};//引用，修改rules时，valInfo.options.rules[element.name]也会被修改
            valInfo.options.messages[element.name] = messages = {};
            
            //遍历adapters数组中的所有元素
            $.each(this.adapters, function () {
                var prefix = "data-val-" + this.name,//this.name获取的是数组元素中 key为name的值，例如：required
                    message = $element.attr(prefix), //根据特性获取值，例如：获取特性 data-val-required的值，也就是错误信息
                    paramValues = {};

                if (message !== undefined) {  // Compare against undefined, because an empty message is legal (and falsy)
                    prefix += "-";
                    //遍历adapters数组中的所有元素中 key等于 param的值，比较的时候会用到
                    $.each(this.params, function () {
                        paramValues[this] = $element.attr(prefix + this);
                    });
                    
                    //执行adapters数组中的元素中 key等于 adapt的值，这个值是一个方法。
                    //执行该方法，为jquery.validate配置信息
                    this.adapt({
                        element: element,
                        form: form,
                        message: message,
                        params: paramValues,
                        rules: rules,//执行该方法时，会将给rules赋值
                        messages: messages
                    });
                }
            });
            console.log(valInfo)
        },

        parse: function (selector) {
            //获取所有的form
            var $forms = $(selector)
                .parents("form")
                .andSelf()
                .add($(selector).find("form"))
                .filter("form");
            //解析html文档中属性 data-val等于true的所有标签
            $(selector).find(":input[data-val=true]").each(function () {
                $jQval.WuPeiqi.parseElement(this, true);
            });
            $forms.each(function () {
                //对每个form配置jqury.validate，例如：错误信息的位置、错误样式
                var info = validationInfo(this);
                if (info) {
                    //使用配置文件对表单进行validate
                    info.attachValidation();
                }
                
            });
        }
    };


    adapters = $jQval.WuPeiqi.adapters;

    adapters.add = function (adapterName, params, fn) {
        if (!fn) {  // Called with no params, just a function
            fn = params;
            params = [];
        }
        this.push({ name: adapterName, params: params, adapt: fn });
        return this;
    };

    adapters.addBool = function (adapterName, ruleName) {
        return this.add(adapterName, function (options) {
            setValidationValues(options, ruleName || adapterName, true);//ruleName || adapterName会自动得到不为空的值
        });
    };

    adapters.addBool("creditcard").addBool("date").addBool("digits").addBool("email").addBool("number").addBool("url");

    adapters.add("equalto", ["other"], function (options) {
        var prefix = getModelPrefix(options.element.name),//获取name属性值的前缀，如果name的值为xx.id，则获取 "xx."；options.element.name=当前标签的name值
            other = options.params.other, //读取当前标签属性 data-val-equalto-other 的值，例如："*.Min"
            fullOtherName = appendModelPrefix(other, prefix), //把 "*."替换为"前缀"，最终得到要 比较 的那个标签的name值
            element = $(options.form).find(":input[name='" + escapeAttributeValue(fullOtherName) + "']")[0]; //获取要去 比较 的那个标签
       
        setValidationValues(options, "equalTo", element);//将validate的规则equalTo添加到 jquery.validate的配置集合中
    });

    adapters.add("required", function (options) {
        // jQuery Validate equates "required" with "mandatory" for checkbox elements
        if (options.element.tagName.toUpperCase() !== "INPUT" || options.element.type.toUpperCase() !== "CHECKBOX") {
            setValidationValues(options, "required", true);
        }
    });

    $(function () {
        $jQval.WuPeiqi.parse(document);
    });
}(jQuery))