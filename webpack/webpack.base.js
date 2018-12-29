"use strict";

const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    target: 'web',
    externals: {},
    context: path.join(path.resolve(), 'decentwork', 'assets'),
    entry: {
        app: './app.js',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use : {
                    loader: 'babel-loader'
                }
            },
            {
                test: /\.(scss|css)$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: "css-loader",
                        options: {
                            minimize: {
                                safe: true
                            }
                        }
                    },
                    {
                        loader: 'postcss-loader', // Run post css actions
                        options: {
                            plugins: function () { // post css plugins, can be exported to postcss.config.js
                                return [
                                    require('precss'),
                                    require('autoprefixer')
                                ];
                            }
                        }
                    },
                    {
                        loader: "sass-loader",
                        options: {}
                    },
                ]
            },
            {
                test: /\.(png|jpe?g|gif|ico)$/,
                loader: 'file-loader?name=assets/images/[name].[hash].[ext]'
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]',
                    outputPath: 'assets/fonts',
                    publicPath: 'assets/fonts/'
                }
            },
	    {
	        test: /\.vue$/,
                loader: 'vue-loader',
	    }
        ]
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: "[name].[hash].css",
            chunkFilename: "[id].[hash].css"
        }),
        new VueLoaderPlugin(),
    ],
    optimization: {
        // Extract shared runtime code.
        runtimeChunk: 'single',
        namedModules: true,
        noEmitOnErrors: true
    }
}
