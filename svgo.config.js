module.exports = {
    // GENERAL OPTIONS
    multipass: true,
    //****** PLUGINS ORDER MATTERS ******** //
    plugins:[
      // MANAGE BUILT-IN DEFAULT PLUGINS
      {
        name: 'preset-default',
        params: {
          overrides: {
            // Set default plugins as disabled with boolean 'false'
            removeViewBox:false, // <-- important
            mergePaths:false, // <-- important
          },
        },
      },
      // MANAGE BUILT-IN NON-DEFAULT PLUGINS
      // Enable non-default plugins
      { name: 'convertTransform' },
      { name: 'removeOffCanvasPaths' }, // last plugin
    ]
  };