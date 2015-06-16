'use strict';

angular.module('myApp.Questions', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/Questions', {
            templateUrl: 'Questions/Questions.html',
            controller: 'QuestionsCtrl'
        });
    }])

    .controller('QuestionsCtrl', function ($scope, $rootScope, $timeout, $modal) {
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

        $scope.addQuestion = function (question) {
            $rootScope.GlobalService.PostQuestion(question.title,question.content,question.category,question.selectedTags).then(function (response) {
                $rootScope.GlobalService.GetQuestions().then(function (response) {
                    $scope.questions = response.data;
                });
            });
        };

        $scope.popupTags = function () {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'tagsPopup.html',
                controller: 'TagsPopupCtrl',
                size: 'sm',
                resolve: {
                    tags: function () {
                        return $scope.tags;
                    }
                }
            });

            modalInstance.result.then(function (selectedItem) {
                $scope.selected = selectedItem;
                $scope.update_questions_list_by_tag(selectedItem.name);
            }, function () {
                $log.info('Modal dismissed at: ' + new Date());
            });
        };

        $scope.newQuestion = function(){
            var questionModal = $modal.open({
                animation: true,
                templateUrl: 'questionPopup.html',
                controller: 'QuestionPopupCtrl',
                size: 'lg',
                resolve: {
                    categories: function () {
                        return $scope.categories;
                    },
                    tags: function () {
                        return $scope.tags;
                    }
                }
            });
            questionModal.result.then(function (newItem) {
                $scope.new = newItem;
                $scope.addQuestion(newItem);
            }, function () {

            });
        };
    })


    .controller('TagsPopupCtrl', function ($scope, $modalInstance, tags) {
        $scope.tags = tags;
        $scope.selected = {
            item: null
        };

        $scope.ok = function () {
            $modalInstance.close($scope.selected.item);
        };
    })

    .controller('QuestionPopupCtrl', function ($scope, $rootScope, $modalInstance, $filter, categories, tags) {
        $scope.allCategories = categories;
        $scope.allTags = tags;
        $scope.newTag = null;
        $scope.new = {
            selectedTags: [] ,
            category: null,
            content: null,
            title: null
        };
        $scope.selected = function(tagId){
            var tmp = $filter('filter')($scope.allTags, {id: tagId});
            var index = $scope.new.selectedTags.indexOf(tmp[0].id);
            if(index > -1){
                $scope.new.selectedTags.splice(index, 1);
            } else {
                $scope.new.selectedTags.push(tmp[0].id);
            }
        };

        $scope.addTag = function () {
            $rootScope.GlobalService.AddTag($scope.newTag).then(function (response) {
                $rootScope.GlobalService.GetTags().then(function (response) {
                    $scope.tags = response.data;
                });
            })
        };
        $scope.add = function () {
            $modalInstance.close($scope.new);
        };
        $scope.cancel = function () {
            $modalInstance.dismiss();
        }
    });


var info_flip = 0;
function moreInfo() {
    if (info_flip == 0) {
        document.getElementById("h2-info").innerHTML = "Strona powstała jako efekt grupowej pracy studentów Politchniki Warszawskiej RB RB BB DF NG JE " +
            "na zaliczenie projektu zespołowego.";
        var d = document.getElementById("h2-info");
        d.className = " animated flipInX hipster-font";
        info_flip = 1
    }
    else {
        document.getElementById("h2-info").innerHTML = "Zadawaj pytania, kto pyta nie błądzi ;) ";
        var d = document.getElementById("h2-info");
        d.className = " animated bounceInUp hipster-font";
        info_flip = 0
    }

}