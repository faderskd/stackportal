'use strict';

angular.module('myApp.Questions', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/Questions', {
            templateUrl: 'Questions/Questions.html',
            controller: 'QuestionsCtrl'
        });
    }])

    .controller('QuestionsCtrl', function ($scope, $rootScope, $timeout) {
        $rootScope.GlobalService.GetQuestions().then(function (response) {
            var questions = response.data;
            $rootScope.GlobalService.GetUsers().then(function (response) {
                var users = response.data;
                var usersDic = {};
                var i;
                for (i = 0; i < users.length; i++)
                    usersDic[users[i].id] = users[i].username;

                for (i = 0; i < questions.length; i++)
                    questions.user = usersDic[questions.user];

                $scope.questions = questions;
            });
        });

        $rootScope.GlobalService.GetCategories().then(function (response) {
            $scope.categories = response.data;
        });

        $rootScope.GlobalService.GetTags().then(function (response) {
            $scope.tags = response.data;
        });

        // przydaloby sie to zamienic na jeden search ale to potem
        // po wybraniu kategori z listy uaktualnia pytania
        $scope.update_questions_list = function () {
            $rootScope.GlobalService.GetQuestionsFromCategory($scope.selected_category.name).then(function (response) {
                $scope.out = $scope.selected_category.name;
                var questions = response.data;
                $rootScope.GlobalService.GetUsers().then(function (response) {
                    var users = response.data;
                    var usersDic = {};
                    var i;
                    for (i = 0; i < users.length; i++)
                        usersDic[users[i].id] = users[i].username;

                    for (i = 0; i < questions.length; i++)
                        questions.user = usersDic[questions.user];

                    $scope.questions = questions;
                });
            });
        };

        // po wybraniu tagu z listy uaktualnia pytania
        $scope.update_questions_list_by_tag = function (tag_name) {
            $rootScope.GlobalService.GetQuestionsFromTag(tag_name).then(function (response) {
                //$scope.out = $scope.selected_tag.name;
                var questions = response.data;
                $rootScope.GlobalService.GetUsers().then(function (response) {
                    var users = response.data;
                    var usersDic = {};
                    var i;
                    for (i = 0; i < users.length; i++)
                        usersDic[users[i].id] = users[i].username;

                    for (i = 0; i < questions.length; i++)
                        questions.user = usersDic[questions.user];

                    $scope.questions = questions;
                });
            });
        };

        $scope.like = function (id) {
            $rootScope.GlobalService.LikeQuestion(id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        var i;
                        for (i = 0; i < $scope.questions.length; i++)
                            if ($scope.questions[i].id == id)
                                $scope.questions[i].likes++;
                    });
                }
            });
        };

        $scope.dislike = function (id) {
            $rootScope.GlobalService.DislikeQuestion(id).then(function (response) {
                if (response.status == 200) {
                    $timeout(function () {
                        var i;
                        for (i = 0; i < $scope.questions.length; i++)
                            if ($scope.questions[i].id == id)
                                $scope.questions[i].dislikes++;
                    });
                }
            });
        };

    });


var info_flip = 0;
function moreInfo() {
    if (info_flip == 0) {
        document.getElementById("h2-info").innerHTML = "Strona powstała jako efekt grupowej pracy studentów Politchniki Warszawskiej RB RB BB DF NG JE na zeliczenie projektu zespolowego.";
        var d = document.getElementById("h2-info");
        d.className = " animated flipInX";
        info_flip = 1
    }
    else {
        document.getElementById("h2-info").innerHTML = "Zadawaj pytania, kto pyta nie błądzi ;) ";
        var d = document.getElementById("h2-info");
        d.className = " animated bounceInUp";
        info_flip = 0
    }

}