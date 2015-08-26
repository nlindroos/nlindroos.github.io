# Biogrid

An Angular application displaying photos and short biographies of selected people including nice animations.

## Architecture

* Latest [AngularJS](http://angularjs.org/) 1.4.4
    * Bootstrapped with [angular-seed](https://github.com/angular/angular-seed)
    * [ng-route](https://code.angularjs.org/1.4.4/angular-route.js)
    * jqLite - subset of jQuery included with AngularJS
* [Twitter Bootstrap](http://getbootstrap.com/)
* [npm](https://www.npmjs.com/) during development
* [lodash](https://lodash.com/)


### Bugs and unfinished features

There is a glitch in the background image when jumping from the first page to the second vice versa that was not fixed due to the time restraint. The image lining should be adjusted to be suitable for both large and small images. The app is in its current form assuming that images are either 282x282 (px) or 585x282 (px). There is a small gap difference based on large/small image order, this could have been finetuned with CSS had there been more time.

Due to the time limitation, touch controls were not implemented. Touch navigation could have easily achieved with ngTouch and $swipe. 


### Technical choices

Although I have used Angular for a couple of months in my current job, I wanted to give developing an ngApp of my own a chance. The app demonstrates Angular's basic components.

To run with Angular was probably not the wisest of choices considering the time limit, as unfamiliarity with starting and setting up the project was time consuming. angular-seed naturally shortened the initial set-up time.

Images are dynamically loaded from the [example project](http://transitions1020.com/#lumia/crew_bios), texts were copied from the same source.

The original idea for image animation was letting the images "drop in" one by one, not requiring scrolling from the user (or in this case pressing the arrow keys). A matte filter (as can be seen on several of the photographs) would have been added to the images and on mouse :focus, the image would have been enriched with the original colors. These features also remain unimplemented due to the restricted time.

In contrast to the example project, there is no need for a re-load on screen resizing as responsive positioning is taken care of by Bootstrap and by custom css. 

All in all the design isn't quite finished but in my opinion the application has potential to be further developed.

The project is hosted on [http://nlindroos.github.io/biogrid/app/index.html](http://nlindroos.github.io/biogrid/app/index.html).

