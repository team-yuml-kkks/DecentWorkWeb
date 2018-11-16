const path          = require('path');
const webpackMerge  = require('webpack-merge');
const baseConfig    = require('./webpack.base.js');
var ManifestPlugin  = require('webpack-manifest-plugin');

module.exports = webpackMerge(baseConfig, {
    output: {
        path: path.resolve(__dirname, path.join(path.resolve(), 'decentwork', 'static', 'dist')),
        filename: '[name].[chunkhash].js'
    },
    plugins: [
        new ManifestPlugin({
            fileName: path.resolve() + '/manifest-dist.json'
        })
    ]
});
