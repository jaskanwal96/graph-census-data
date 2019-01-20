app.controller('MainController', ['$scope', '$http', '$log', function($scope, $http, $log){
  }]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); ;