(function() {
var initChessBoard = function() {
    var jqEtude = $(this);
    jqEtude.chess({ 
        // pgn: jqEtude.data('pgn')
        fen: jqEtude.data('fen'),
        square_size: 24
    });
};

$(document).ready(function() {
    $('.etudes-list .etude-preview').each(initChessBoard);
});
}());
