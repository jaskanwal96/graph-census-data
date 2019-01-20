app.controller('SearchController', ['$scope', '$http', '$log', function($scope, $http, $log){
   $http.get('/getCensusData/1').
      success(function(results) {
        $log.log(results);
        $scope.fields = results.data
      }).
      error(function(error) {
        $log.log(error);
      });

      $scope.submit = function() {
        let sex = [];
        if($scope.sex1)sex.push(" Male");
        if($scope.sex2)sex.push(" Female");
        
        let rel = [];

        if($scope.rel1)rel.push(" Unmarried");
        if($scope.rel2)rel.push(" Own-child"); 
        if($scope.rel3)rel.push(" Wife");
        if($scope.rel4)rel.push(" Husband");
        if($scope.rel5)rel.push(" Other-relative");
        if($scope.rel6)rel.push(" Not-in-family");
        
        let race = []
        if($scope.race1)race.push(" White");
        if($scope.race2)race.push(" Black"); 
        if($scope.race3)race.push(" Asian-Pac-Islander");
        if($scope.race4)race.push(" Amer-Indian-Eskimo");
        if($scope.race5)race.push(" Other");
        
        $log.log(sex, rel, race);
        
        $http({
          url: '/getCensusData/',
          method: "POST",
          headers: { 'Content-Type': 'application/json'},
          data: JSON.stringify({sex: sex, relationship : rel, race: race})
        }).success(function(results) {
          $scope.fields = results.data
        }).error(function(error) {
          $log.log(error);
        });
        
      };
      $scope.fields = null;
  }]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
 }); ;