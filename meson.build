project('pop-icon-theme',
    version: '0.1',
    meson_version: '>= 0.40',
    license: 'CC-by-SA',
    default_options: ['prefix=/usr']
)

install_subdir('Pop',
    install_dir: join_paths(get_option('prefix'), 'share/icons')
)

install_subdir('Pop-Dark',
    install_dir: join_paths(get_option('prefix'), 'share/icons')
)

meson.add_install_script('meson/post_install.py')
