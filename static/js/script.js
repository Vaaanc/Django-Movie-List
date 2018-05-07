$(document).ready(function(){
  $('#modalDelete').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var recipient = button.data('name')
    var modal = $(this)
    modal.find('.modal-body p').text("Are you sure you want to delete " + recipient)
    modal.find('.modal-body form').attr("action", button.data('url'))
  })

    $('.likes').on('click', function(){
      var movie_id, movie_slug;
      button = $(this)
      movie_slug = $(this).attr("data-slug");
      movie_id = $(this).attr("data-movieid");
      $.get('/movie/'+movie_slug+'/like/', {movie_id: movie_id}, function(data){
        button.hide();
        button.next('#like_count').html('Likes: '+data);
    });
  });
  
  showMovieCards();
  function showMovieCards(){
    var time = 0
    $('.movie-card').each(function() {
      var $this = $(this);
      setTimeout( function(){
        $this.css({
          'transform': 'translateY(0)',
          'opacity' : '1'
        });
      }, time)
      time += 300;
    });
  }
});
