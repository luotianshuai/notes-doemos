export const breakpoints = {
    xs: 480,
    sm: 576,
    md: 768,
    lg: 992,
    xl: 1200,
    xxl: 1600,
};

export default {
    spacing: value => value * 8,
    palette: {
        primary: '#7E8AEF',
        link: '#6E7DF9',
        success: '#52c41a',
        warning: '#faad14',
        error: '#f5222d',
        heading: 'rgba(42, 42, 68, 1)',
        text: 'rgba(42, 42, 68, .8)',
        textSecondary: 'rgba(42, 42, 68, .6)',
        disabled: 'rgba(42, 42, 68, .3)',
        border: 'rgba(229, 229, 241, 1)',
        primaryDark: '#6F77AA',
        white: '#fff',
    },
    shadows: [
        '0 2px 8px rgba(0, 0, 0, .15)',
    ],
    shape: {
        borderRadius: 4,
    },
    breakpoints: {
        keys: ['xs', 'sm', 'md', 'lg', 'xl', 'xxl'],

        up: function up(key) {
            return '@media (min-width:'.concat(breakpoints[key], 'px)');
        },
    },
    bodyMinWidth: 1280,
    zIndex: {
        tableFixed: 'auto',
        affix: 10,
        backTop: 10,
        badge: 10,
        pickerPanel: 10,
        popupClose: 10,
        modal: 1001,
        modalMask: 1001,
        message: 1010,
        notification: 1010,
        popover: 1030,
        dropdown: 1050,
        picker: 1050,
        tooltip: 1060,
    },
    slideSwitch: {
        bgColor: '#313350',
        slideColor: '#F9F9FF',
    },
};
