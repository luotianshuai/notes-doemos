#!/bin/bash

IS_OPEN=false


HOST_NAME0=$(sogou-host |grep "small.novel.tc.ted")
HOST_NAME1=$(sogou-host |grep "pushpro01.novel.tc.ted")
HOST_NAME2=$(sogou-host |grep "pushpro02.novel.tc.ted")
HOST_NAME3=$(sogou-host |grep "pushpro03.novel.tc.ted")
HOST_NAME4=$(sogou-host |grep "pushpro04.novel.tc.ted")


if [[ ${HOST_NAME0} ]];then
    cat <<EOF
#online person task
interface.personal.job.open=false

personal.data.section=1/4
#job rate for variable

#online
person.host=http://recommend.wechat.novel.sogou

EOF
fi

if [[ ${HOST_NAME1} ]];then
    cat <<EOF
#online person task
interface.personal.job.open=${IS_OPEN}

personal.data.section=1/4
#job rate for variable

#online
person.host=http://recommend.wechat.novel.sogou

EOF
fi

if [[ ${HOST_NAME2} ]];then
    cat <<EOF
#online person task
interface.personal.job.open=${IS_OPEN}

personal.data.section=2/4
#job rate for variable

#online
person.host=http://recommend.wechat.novel.sogou

EOF
fi

if [[ ${HOST_NAME3} ]];then
    cat <<EOF
#online person task
interface.personal.job.open=${IS_OPEN}

personal.data.section=3/4
#job rate for variable

#online
person.host=http://recommend.wechat.novel.sogou

EOF
fi

if [[ ${HOST_NAME4} ]];then
    cat <<EOF
#online person task
interface.personal.job.open=${IS_OPEN}

personal.data.section=4/4
#job rate for variable

#online
person.host=http://recommend.wechat.novel.sogou

EOF
fi