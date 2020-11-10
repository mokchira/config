import dracula.draw

#load existing settings made via :set
config.load_autoconfig()

dracula.draw.blood(c, {
    'spacing': {
        'vertical': 4,
        'horizontal': 6
        }
    })

config.bind('<Ctrl-R>', 'config-cycle content.user_stylesheets ~/Util/dracula.css ~/Util/qutebrowser_dark_solarized/solarized-dark.css ""')


