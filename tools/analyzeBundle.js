'use strict';

import { BundleAnalyzerPlugin } from 'webpack-bundle-analyzer';
import webpack from 'webpack';

import config from '../webpack.config.prod';

config.plugins.push(new BundleAnalyzerPlugin());

const compiler = webpack(config);

compiler.run((error, stats) => {
    if (error) {
        throw new Error(error);
    }

    console.log(stats); // eslint-disable-line no-console
});
