'use strict';

angular.module('myApp.Question', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/Question/:questionId', {
    templateUrl: 'Question/Question.html',
    controller: 'QuestionCtrl'
  });
}])

.controller('QuestionCtrl',function($scope, $routeParams, $rootScope) {
      $rootScope.GlobalService.GetQuestion($routeParams.questionId).then(function (response) {
        $scope.question = response.data;
        var i;
        $scope.answers = [];
        for (i = 0; i < $scope.question.answers.length; i++)
        {
          $rootScope.GlobalService.GetAnswer($scope.question.answers[i]).then(function (response) {
            $scope.answers.push(response.data);
          });
        }
      });
});