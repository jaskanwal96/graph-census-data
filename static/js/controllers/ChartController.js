app.controller('ChartController', function($scope, $http, $log) {
    //chart definition
    $http.get('/getSexData').
      success(function(results) {
        $log.log("Helloooo",results.Male);
        $scope.dataSource = {
                "chart": {
                    "caption": "Census 1996",
                    "subCaption" : "Male-Female Ratio",
                    "showValues":"1",
                    "enableMultiSlicing":"1",
                    "theme": "fusion"
                },
                "data": [{
                    "label": "Male",
                    "value": results.Male
                }, {
                    "label": "Female",
                    "value": results.Female
                }]
            };

      }).
      error(function(error) {
        $log.log(error);
      });

      $http.get('/getRelationshipData').
      success(function(results) {
        $log.log(results);
        $scope.relationDataSource = {
            "chart" : {
                "caption": "Census 1996",
                "subCaption" : "Relationship Graph",
                "xaxisname": "Relationship",
                "yaxisname": "Count",
                "showValues":"1",
                "theme": "fusion"
            },
            "data" : results.data,
        }

      }).
      error(function(error) {
        $log.log(error);
      });
    $scope.dataSource =  {}
    $scope.relationDataSource  = {}
});