let strigifyBoard = function (board){
    return board[0].join('    ') + '\n' +
            board[1].join('    ') + '\n' +
            board[2].join('    ') + '\n';
}


let didWeWin = function(board, player){
    // check rows
    if (board[0][0] === player && board[0][1] === player && board[0][2] === player)
        return true;
    if (board[1][0] === player && board[1][1] === player && board[1][2] === player)
        return true;
    if (board[2][0] === player && board[2][1] === player && board[2][2] === player)
        return true;

    // check columns
    if (board[0][0] === player && board[1][0] === player && board[2][0] === player)
        return true;
    if (board[0][1] === player && board[1][1] === player && board[2][1] === player)
        return true;
    if (board[0][2] === player && board[1][2] === player && board[2][2] === player)
        return true;

    // check diagonal
    if (board[0][0] === player && board[1][1] === player && board[2][2] === player)
        return true;
    if (board[0][2] === player && board[1][1] === player && board[2][0] === player)
        return true;

    return false;
}


let isFull = function (board){
    let i = 0;
    while (i < board.length){
        const row = board[i];
        let j = 0;
        while (j < row.length){
            if (row[i] === "_")
                return false;
            j++;
        }
        i++;
    }
    return true;
}


let board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
];

let player = "x";


while (true){
    let boardStr = strigifyBoard(board)

    let row = +prompt("Enter a row: \n" + boardStr);
    let column = +prompt("Enter a column: \n" + boardStr);

    if (board[row][column] !== "_"){
        alert("Not a legal move, you lose!");
        break;
    }

    board[row][column] = player;
    const won = didWeWin(board, player);

    if (won){
        alert(`Player ${player} won the game!`);
        break;
    }

    if (isFull(board)){
        alert("The board is full, nobady won!");
        break;
    }
    
    if (player === "x"){
        player = "o";
    } else{
        player = "x";
    }
}
