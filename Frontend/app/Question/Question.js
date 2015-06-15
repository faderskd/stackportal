'use strict';

angular.module('myApp.Question', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/Question/:questionId', {
            templateUrl: 'Question/Question.html',
            controller: 'QuestionCtrl'
        });
    }])

    .controller('QuestionCtrl', function ($scope, $routeParams, $rootScope, $location, $anchorScroll, $route, $timeout, $cookies) {
        $location.hash('top');
        $scope.qContent = "";
        $rootScope.GlobalService.GetQuestion($routeParams.questionId).then(function (response) {
            $scope.question = response.data;
            if ($scope.question.user == $cookies.get('userId'))
                $scope.isAuthor = true;
            var i, j;
            var commentsId = $scope.question.comments;
            $scope.question.comments = [];
            for (j = 0; j < commentsId.length; j++) {
                $rootScope.GlobalService.GetComment(commentsId[j]).then(function (response) {
                    $scope.question.comments.push(response.data);
                });
            }
            $scope.answers = [];
            for (i = 0; i < $scope.question.answers.length; i++) {
                $rootScope.GlobalService.GetAnswer($scope.question.answers[i]).then(function (response) {
                    var answer = response.data;
                    commentsId = answer.comments;
                    answer.comments = [];
                    for (j = 0; j < commentsId.length; j++) {
                        $rootScope.GlobalService.GetComment(commentsId[j]).then(function (response) {
                            answer.comments.push(response.data);
                        });
                    }
                    $scope.answers.push(answer);
                });
            }
        });

        $scope.Send = function () {
            $rootScope.GlobalService.PostAnswer($scope.question.id, $scope.formAnswer);
            $route.reload();
        };

        $scope.likeQ = function () {
            $rootScope.GlobalService.LikeQuestion($scope.question.id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        $scope.question.likes++;
                    });
                }
            });
        };

        $scope.dislikeQ = function () {
            $rootScope.GlobalService.DislikeQuestion($scope.question.id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        $scope.question.dislikes++;
                    });
                }
            });
        };

        $scope.likeA = function (id) {
            $rootScope.GlobalService.LikeAnswer(id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        var i;
                        for (i = 0; i < $scope.answers.length; i++)
                            if ($scope.answers[i].id == id)
                                $scope.answers[i].likes++;
                    });
                }
            });
        };

        $scope.dislikeA = function (id) {
            $rootScope.GlobalService.DislikeAnswer(id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        var i;
                        for (i = 0; i < $scope.answers.length; i++)
                            if ($scope.answers[i].id == id)
                                $scope.answers[i].dislikes++;
                    });
                }
            });
        };

        $scope.markAnswer = function (id) {
            $rootScope.GlobalService.MarkAnswer(id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        var i;
                        for (i = 0; i < $scope.answers.length; i++)
                            if ($scope.answers[i].id == id) {
                                $scope.answers[i].solved = true;
                                $scope.question.solved = true;
                            }
                    });
                }
            });
        };

        $scope.Comment = function (questionId, answerId) {
            var content = $scope.qContent;
            if (answerId != null)
                for (i = 0; i < $scope.answers.length; i++)
                    if ($scope.answers[i].id == id)
                        content = $scope.answers[i].commentContent;
            $rootScope.GlobalService.PostComment(questionId, answerId, content).then(function (response) {
                if (response.status == 201) {
                    $timeout(function () {
                        var i;
                        if (answerId != null)
                            for (i = 0; i < $scope.answers.length; i++) {
                                if ($scope.answers[i].id == id)
                                    $scope.answers[i].comments.push(response.data);
                            }
                        else {
                            $scope.question.comments.push(response.data);
                            $scope.qComment = !$scope.qComment;
                        }
                    });
                }
            });
        };
    });