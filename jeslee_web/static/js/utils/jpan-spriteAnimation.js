jpan = {

   /**
    * When the mouse moves it is followed by stardust.
    */
   stardust: function(params) {
      var spriteImage = params && params.spriteImage ? params.spriteImage : 'gfx/stardust.png'; // the image to show a png sprite.
      if ($ === undefined)
      {
         $ = jQuery;
      }
      $('body').mousemove(function(event) {
         //    $('body').click(function(event) {
         if (parseInt(Math.random() * 3) == 1) {
            var randomX = parseInt(Math.random() * 4) - 2;
            var randomY = parseInt(Math.random() * 4) - 2;
            var starEffect = {
               spriteImage: spriteImage,
               xPos:event.pageX - 6 + randomX,
               yPos:event.pageY - 6 + randomY,
               xDrift:randomX * 3,
               yDrift:randomY * 3,
               btTop:0,
               frames:4,
               frameSize: 5,
               frameRate:200
            };
            jpan.animateSprite(starEffect); // run the sprite animation
         }
      });
   },

   animatePoof: function (event, params) {
      var spriteImage = params && params.spriteImage ? params.spriteImage : 'gfx/poof.png'; // the image to show a png sprite.
      var poofEffect = {
         xPos: event.pageX - 20,
         yPos: event.pageY - 20,
         spriteImage: spriteImage,
         xOffset:24,
         yOffset:24,
         btTop:0,
         frames:5,
         frameSize: 32,
         frameRate:200
      };
      jpan.animateSprite(poofEffect);
   },
   /**
    * Animates a sprite at the location of the passed x and y Position..
    * @param options
    */
   animateSprite: function (options) {
      if ($ === undefined)
      {
         $ = jQuery;
      }
      var xPos = options && options.xPos ? options.xPos : null; // the x position where to animate the sprite
      var yPos = options && options.yPos ? options.yPos : null; // the y position where to animate the sprite
      var spriteImage = options && options.spriteImage ? options.spriteImage : 'gfx/poof.png'; // the image to show a png sprite.
      var cssPath = options && options.cssPath ? options.cssPath : null; // the image to show a png sprite.
      var xDrift = options && options.xDrift ? options.xDrift : null; // move xDrift on the x-axis every time the next frame is shown
      var yDrift = options && options.yDrift ? options.yDrift : null; // move yDrift on the y-axis every time the next frame is shown
      var bgTop = options && options.btTop ? options.btTop : 0; // initial background-position for the poof sprit is '0 0'
      var frames = options && options.frames ? options.frames : 5; // number of frames in the sprite animation
      var frameSize = options && options.frameSize ? options.frameSize : 32; // size of poof <div> in pixels (32 x 32 px in this example)
      var frameRate = options && options.frameRate ? options.frameRate : 80; // set length of time each frame in the animation will display (in milliseconds)

      if (!cssPath) {
         var newSpriteElement = document.createElement("div");
         $('body').append(newSpriteElement);
         var spriteIdValue = 'animateSprite_' + parseInt(Math.random() * 10000);
         $(newSpriteElement).attr('id', spriteIdValue);
         cssPath = '#' + spriteIdValue;
      }
      // set style of element
      $(cssPath).css({
         background: 'transparent url(' + spriteImage + ') no-repeat 0 0',
         left: xPos + 'px',
         top: yPos + 'px',
         height: frameSize,
         width: frameSize,
         position: 'absolute'
      }).show(); // display the poof <div>
      // loop through amination frames
      // and display each frame by resetting the background-position of the poof <div>
      for (var i = 1; i < frames; i++) {
         $(cssPath).animate({
            backgroundPosition: '0 ' + (bgTop - frameSize) + 'px',
            left: (xPos + i * xDrift) + 'px',
            top: (yPos + i * yDrift) + 'px'
         }, frameRate);
         bgTop -= frameSize; // update bgPosition to reflect the new background-position of our poof <div>
      }
      // wait until the animation completes and then hide the poof <div>
      setTimeout("$('" + cssPath + "').hide()", frames * frameRate);
   }
};

// added animate sprite a function to jQuery
jQuery.fn.animateSprite = jpan.animateSprite;
