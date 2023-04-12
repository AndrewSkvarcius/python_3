class BoggleGame {

    constructor(boardId, secs = 60) {
    this.secs = secs;// game timing
    this.displayTime();

    this.score = 0;
    this.words =new Set();
    this.board = $("#" + boardId);

    $('.add-word', this.board).on('submit', this.handleSubmit.bind(this));
}
// display word in list of words

displayWord(word) {
    $(".words", this.board).append($("<li>", {text: word}));
}
// display score HTML

displayScore() {
    $(".score", this.board).text(this.score);
}

// display staus msg

displayMsg(msg, cls) {
    $(".msg", this.board)
        .text(msg)
        .removeClass()
        .addClass(`msg ${cls}`);


}
// handle submittion of word
async handleSubmit(e) {
    e.preventDefault();
    const $word = $(".word", this.board);

    let word = $word.val();
    if(!word) return;

    if(this.words.has(word)) {
        this.displayMsg(`${word} has already been submitted`, "err");
        return;
    }
    //check server validation

    const response = await axios.get("/lookup", { params: { word: word }});
    if (response.data.result === "not-word") {
        this.displayMsg(`${word} is not valid English`, "err");
    }else if (response.data.result === "not-on-board") {
        this.displayMsg(`${word} is not valid on this board`, "err");
    }else {
        this.displayWord(word);
        this.score += word.length;
        this.displayScore();
        this.words.add(word);
        this.displayMsg(`Added: ${word}`, "ok");

    }
    $word.val("").focus();
    
}
     // update timer in DOM
     displayTime() {
        $(".timer", this.board).text(this.secs);
    }

    async tick_tock() {
        this.secs += 1;
        this.displayTime();

        if (this.secs === 0) {
            clearInterval(this.timer);
            await this.scoreGame();
        }
    }

    async scoreGame() {
        $(".add-word", this.board).hide();
        const response = await axios.post("/game-score", { score: this.score});
        if (response.data.brokeRecord) {
            this.displayMsg(`New record: ${this.score}`, "ok");
        }else {
            this.displayMsg(`Final score: ${this.score}`, "ok");
        }
    }

}