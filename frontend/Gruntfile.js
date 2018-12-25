module.exports = function(grunt) {
    "use strict"

    grunt.initConfig({
        concurrent: {
            "prod": {
                tasks: ["nodemon:prod", "watch"],
                options: {
                    logConcurrentOutput: true
                }
            }

        },

        nodemon: {
            prod: {
                script: "bin/www.js",
                options: {
                    nodeArgs: [],
                    env: {
                        NODE_ENV: "production"
                    },
                    ignore: [
                        "node_modules/**",
                        "static/**"
                    ],
                    callback: function (nodemon) {
                        //console.log(arguments);
                    }
                }
            }
        },
        watch: {
            static: {
                files: ["static/**"],
                options: {
                    livereload: true
                }
            },

            templates: {
                files: ["views/**"],
                options: {
                    livereload: true
                }
            }
        },
        'node-inspector': {
            dev: {}
        }
    });

    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-nodemon');
    grunt.loadNpmTasks('grunt-concurrent');
    grunt.loadNpmTasks('grunt-node-inspector');

    grunt.registerTask("default", ["concurrent:prod"]);
}
