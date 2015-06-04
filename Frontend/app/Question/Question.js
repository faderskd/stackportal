'use strict';

angular.module('myApp.Question', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/Question/:questionId', {
    templateUrl: 'Question/Question.html',
    controller: 'QuestionCtrl'
  });
}])

.controller('QuestionCtrl',function($scope, $routeParams, $rootScope, $location, $anchorScroll, $route) {
      $location.hash('top');
      $rootScope.GlobalService.GetQuestion($routeParams.questionId).then(function (response) {
        $scope.question = response.data;
        var i, j;
        var commentsId = $scope.question.comments;
        $scope.question.comments = [];
        for (j = 0; j < commentsId.length; j++)
        {
          $rootScope.GlobalService.GetComment(commentsId[j]).then(function (response) {
            $scope.question.comments.push(response.data);
          });
        }
        $scope.answers = [];
        for (i = 0; i < $scope.question.answers.length; i++)
        {
          $rootScope.GlobalService.GetAnswer($scope.question.answers[i]).then(function (response) {
            var answer = response.data;
            commentsId = answer.comments;
            answer.comments = [];
            for (j = 0; j < commentsId.length; j++)
            {
              $rootScope.GlobalService.GetComment(commentsId[j]).then(function (response) {
                answer.comments.push(response.data);
              });
            }
            $scope.answers.push(answer);
          });
        }
      });

      $scope.Send = function()
      {
        $rootScope.GlobalService.PostAnswer($scope.question.id, $scope.formAnswer);
        $route.reload();
      }
});