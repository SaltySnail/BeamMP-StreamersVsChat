angular.module('beamng.apps')
.directive('svc', ['CanvasShortcuts','$timeout', function (CanvasShortcuts, $timeout) {
  return {
    template:  `
	<div id="svcDiv" style="height:100%; width:100%; margin:0px; background:transparent;" layout="row" layout-align="center left" layout-wrap> 
		<img ng-repeat="fimage in fullscreenImages" id="{{fimage.id}}" ng-src="{{fimage.path}}" alt="Fullscreen Image" style="position: fixed; top: 0; left: 0; min-height: 100%;">
		<img ng-repeat="image in images" id="{{image.id}}" ng-src="{{image.path}}" alt="Drifting Image" style="position: absolute;">
	</div>
    `,
    replace: true,
    restrict: 'EA',
    link: function (scope, element, attrs) {
		var dx = [2, 3]; // Change in x for each image
		var dy = [2, 3]; // Change in y for each image
		var x = [0, 50]; // Initial x for each image
		var y = [0, 50]; // Initial y for each image
		var timerID = {};
		
		scope.inactiveImages = [
			{id: 'SnoopDogg', path: 'SnoopDogg.gif'}
		]; // Set the image paths here
		
		scope.images = [
		];

		scope.inactiveFullscreenImages = [
			// {id: 'SmokeScreen', path: 'SmokeScreen.gif'},
			{id: 'Smog', path: 'Smog.gif'}
		]; // Set the image paths here

		scope.fullscreenImages = [
		];

		function driftImage() {
			for (var i = 0; i < scope.images.length; i++) {
				// console.log("ScopeImage stuff: " + scope.images[i].id);
				var img = document.getElementById(scope.images[i].id);
				if (!img) return;

				var width = divWidth - img.width;
				var height = divHeight - img.height;

				if (x[i] > width || x[i] < 0) {
					dx[i] = -dx[i]; // Reverse direction
				}
				if (y[i] > height || y[i] < 0) {
					dy[i] = -dy[i]; // Reverse direction
				}

				x[i] += dx[i];
				y[i] += dy[i];

				img.style.left = x[i] + 'px';
				img.style.top = y[i] + 'px';
			}
		}

	var divHeight = 0;
	var divWidth = 0;

	angular.element(document).ready(function () {
		var svcDiv = document.getElementById('svcDiv');
		if (!svcDiv) return;
		divHeight = svcDiv.offsetHeight;
		divWidth = svcDiv.offsetWidth;
	});
	

	scope.$on('svcRemoveFullscreenImage', function (event, path) {
		var index = scope.fullscreenImages.findIndex(function(image) {
			return image.path === path;
		});
		if (index !== -1) {
			scope.inactiveFullscreenImages.push(scope.fullscreenImages[index]);
			scope.fullscreenImages.splice(index, 1);
		}
	});
	
	scope.$on('svcAddFullscreenImage', function (event, path) {
		var index = scope.inactiveFullscreenImages.findIndex(function(image) {
			return image.path === path;
		});
		if (index !== -1) {
			scope.fullscreenImages.push(scope.inactiveFullscreenImages[index]);
			scope.inactiveFullscreenImages.splice(index, 1);
		}
	});

	scope.$on('svcRemoveDVDImage', function (event, path) {
		var index = scope.images.findIndex(function(image) {
			return image.path === path;
		});
		if (index !== -1) {
			scope.inactiveImages.push(scope.images[index]);
			scope.images.splice(index, 1);
		}
		clearInterval(timerID[path]);
	});

	scope.$on('svcAddDVDImage', function (event, path) {
		var index = scope.inactiveImages.findIndex(function(image) {
			return image.path === path;
		});
		if (index !== -1) {
			scope.images.push(scope.inactiveImages[index]);
			scope.inactiveImages.splice(index, 1);
		}
		timerID[path] = setInterval(driftImage, 10);
	});
	}}}])