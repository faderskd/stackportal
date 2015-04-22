'use strict';

angular.module('myApp.Questions', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/Questions', {
    templateUrl: 'Questions/Questions.html',
    controller: 'QuestionsCtrl'
  });
}])

.controller('QuestionsCtrl', function($scope, $rootScope) {
      $rootScope.GlobalService.GetQuestions().then(function (response) {
        $scope.questions = response.data;
      });


        $rootScope.GlobalService.GetTags().then(function (response) {
            $scope.tags = response.data;
        });
});