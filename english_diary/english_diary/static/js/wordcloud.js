$( document ).ready(function() {
      var wholeWords = $("#wordcloud").data("words");
      var regExpSpecial = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"\“\”\’]/gi;
      var regExpNumber = /[0-9]/g;

      var fill = d3.scale.category20();
      var minimumFontsize = 14;
      var maximumFontsize = 150;

      wholeWordsOnlyAlpha = wholeWords
        .replace(regExpSpecial, '')
        .replace(regExpNumber, '')
        .split(' ');
      wordsObj = wordsFrequencies(wholeWordsOnlyAlpha);
      words = Object.keys(wordsObj).map(function(word) {
        // if word's length is smaller 2, do not show on wordcloud
        // 100th frequency is font-size mixium
        if( word.length >= 3){
          return {text: word, size: maximumFontsize/2 * ( Math.log10(wordsObj[word]) )}; }
        else { return {text: "", size:0 }; }
      })//.concat([{text:"OneBigWord", size: 50}]);

      var maxSize = d3.max(words, function(d) { return d.size; });
      var minSize = d3.min(words, function(d) { return d.size; });
      var fontScale = d3.scale.linear() // scale algo which is used to map the domain to the range
        .domain([minSize, maxSize]) //set domain which will be mapped to the range values
        .range([minimumFontsize, maximumFontsize]); // set min/max font size

      function draw(words) {
        d3.select("body").append("svg")
          .attr("width", 500)
          .attr("height", 500)
          .style("background-color", "#000000")
        .append("g")
          .attr("transform", "translate(250,250)")
        .selectAll("text")
          .data(words)
        .enter().append("text")
          .style("font-size", function(d) { return d.size + "px"; })
          .style("font-family", "Arial")
          .style("fill", function(d, i) { return fill(i); })
          .attr("text-anchor", "middle")
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; });
      }

      function wordsFrequencies(words) {
          return words.reduce(function(frequencies, word) {
              frequencies[word] = (frequencies[word] || 0) + 1;
              return frequencies;
          }, {});
      }

      d3.layout.cloud().size([500, 500])
        .words(words)
        .padding(5)
        .rotate(function() {
          // return ~~(Math.random() * 2) * 90;
          return 0;
        })
        // .font("Impact")
        .fontSize(function(d) { return fontScale(d.size) }) // the d3 scale function is used here
        .on("end", draw)
        .start();
});
