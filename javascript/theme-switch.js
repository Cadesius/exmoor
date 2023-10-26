var themes = [
    // Dark theme
    {
        "background-colour" : "#262626",
        "text-colour" : "#ffffff",
        "alt-text-colour" : "#ffffff",
        "transparency-colour" : "#00000000",
        "modal-background-colour" : "#262626fc"
    },
    // Light theme
    {
        "background-colour" : "#ffffff",
        "text-colour" : "#262626",
        "alt-text-colour" : "#000000",
        "transparency-colour" : "#00000000",
        "modal-background-colour" : "#fffffffc"
    }
];

// var theme = "dark"
var selection = 1

function switchTheme () {
    if (document.cookie.includes ("dark")) {
        selection = 1
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled-inverted.png"
        });
        document.getElementById ("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    } if (document.cookie.includes ("light")) {
        selection = 0
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled.png"
        });
        document.getElementById("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    }
};

function switchCookie () {
    if (document.cookie.includes ("dark")) {
        document.cookie = "theme:light;"
    } else {
        document.cookie = "theme:dark;"
    }
};

if (document.cookie.includes ("theme")) {
    if (document.cookie.includes ("dark")) {
        // console.log ("Cookie already exists - set dark mode")
        selection = 0
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled.png"
        });
        document.getElementById("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    } if (document.cookie.includes ("light")) {
        // console.log ("Cookie already exists - set light mode")
        selection = 1
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled-inverted.png"
        });
        document.getElementById ("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    }
} else {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        document.cookie = "theme:dark;"
        selection = 0;
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled.png";
        });
        document.getElementById("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    } else {
        document.cookie = "theme:light;"
        selection = 1;
        for (let theme in themes [selection]) {
            document.documentElement.style.setProperty("--" + theme, themes [selection] [theme]);
        }
        var home_icons = document.querySelectorAll (".modal_home_icon");
        home_icons.forEach(element => {
            element.src = "media/home-icon/home-icon-filled-inverted.png";
        });
        document.getElementById ("theme-switch-icon").src = "media/theme-switch-icon/theme-switch-icon-inverted.png";
    };
};