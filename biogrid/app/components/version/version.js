'use strict';

angular.module('bioGrid.version', [
  'bioGrid.version.interpolate-filter',
  'bioGrid.version.version-directive'
])

.value('version', '0.1');
