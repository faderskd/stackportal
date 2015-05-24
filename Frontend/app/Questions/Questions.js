'use strict';

angular.module('myApp.Questions', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/Questions', {
    templateUrl: 'Questions/Questions.html',
    controller: 'QuestionsCtrl'
  });
    }])

    .controller('QuestionsCtrl', function ($scope, $rootScope) {
        $rootScope.GlobalService.GetQuestions().then(function (response) {
            $scope.questions = response.data;
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
                $scope.questions = response.data;
            });
        };

        // po wybraniu tagu z listy uaktualnia pytania
        $scope.update_questions_list_by_tag = function (tag_name) {
            $rootScope.GlobalService.GetQuestionsFromTag(tag_name).then(function (response) {
                //$scope.out = $scope.selected_tag.name;
                $scope.questions = response.data;
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