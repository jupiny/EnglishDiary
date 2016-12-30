$( document ).ready(function() {
      var wholeWords = $("#wordcloud").data("words"),
          w = window.innerWidth,
          h = window.innerHeight;

      var wordNumbers = /[0-9]/g,
          punctuation = /[\{\}\[\]\/?.,;:|\)*~`!^\_+<>@\#$%&\\\=\(\'\"\“\”\‘\’]/gi,
          stopWords = /^(i|me|my|myself|we|us|our|ours|ourselves|you|your|yours|yourself|yourselves|he|him|his|himself|she|her|hers|herself|it|its|itself|they|them|their|theirs|themselves|what|which|who|whom|whose|this|that|these|those|am|is|are|was|were|be|been|being|have|has|had|having|do|does|did|doing|will|would|should|can|could|ought|i'm|you're|he's|she's|it's|we're|they're|i've|you've|we've|they've|i'd|you'd|he'd|she'd|we'd|they'd|i'll|you'll|he'll|she'll|we'll|they'll|isn't|aren't|wasn't|weren't|hasn't|haven't|hadn't|doesn't|don't|didn't|won't|wouldn't|shan't|shouldn't|can't|cannot|couldn't|mustn't|let's|that's|who's|what's|here's|there's|when's|where's|why's|how's|a|an|the|and|but|if|or|because|as|until|while|of|at|by|for|with|about|against|between|into|through|during|before|after|above|below|to|from|up|upon|down|in|out|on|off|over|under|again|further|then|once|here|there|when|where|why|how|all|any|both|each|few|more|most|other|some|such|no|nor|not|only|own|same|so|than|too|very|say|says|said|shall|one|two|three|four|five|six|seven|eight|nine|ten|)$/gi;
          // unicodePunctuationRe = "!-#%-*,-/:;?@\\[-\\]_{}\xa1\xa7\xab\xb6\xb7\xbb\xbf\u037e\u0387\u055a-\u055f\u0589\u058a\u05be\u05c0\u05c3\u05c6\u05f3\u05f4\u0609\u060a\u060c\u060d\u061b\u061e\u061f\u066a-\u066d\u06d4\u0700-\u070d\u07f7-\u07f9\u0830-\u083e\u085e\u0964\u0965\u0970\u0af0\u0df4\u0e4f\u0e5a\u0e5b\u0f04-\u0f12\u0f14\u0f3a-\u0f3d\u0f85\u0fd0-\u0fd4\u0fd9\u0fda\u104a-\u104f\u10fb\u1360-\u1368\u1400\u166d\u166e\u169b\u169c\u16eb-\u16ed\u1735\u1736\u17d4-\u17d6\u17d8-\u17da\u1800-\u180a\u1944\u1945\u1a1e\u1a1f\u1aa0-\u1aa6\u1aa8-\u1aad\u1b5a-\u1b60\u1bfc-\u1bff\u1c3b-\u1c3f\u1c7e\u1c7f\u1cc0-\u1cc7\u1cd3\u2010-\u2027\u2030-\u2043\u2045-\u2051\u2053-\u205e\u207d\u207e\u208d\u208e\u2329\u232a\u2768-\u2775\u27c5\u27c6\u27e6-\u27ef\u2983-\u2998\u29d8-\u29db\u29fc\u29fd\u2cf9-\u2cfc\u2cfe\u2cff\u2d70\u2e00-\u2e2e\u2e30-\u2e3b\u3001-\u3003\u3008-\u3011\u3014-\u301f\u3030\u303d\u30a0\u30fb\ua4fe\ua4ff\ua60d-\ua60f\ua673\ua67e\ua6f2-\ua6f7\ua874-\ua877\ua8ce\ua8cf\ua8f8-\ua8fa\ua92e\ua92f\ua95f\ua9c1-\ua9cd\ua9de\ua9df\uaa5c-\uaa5f\uaade\uaadf\uaaf0\uaaf1\uabeb\ufd3e\ufd3f\ufe10-\ufe19\ufe30-\ufe52\ufe54-\ufe61\ufe63\ufe68\ufe6a\ufe6b\uff01-\uff03\uff05-\uff0a\uff0c-\uff0f\uff1a\uff1b\uff1f\uff20\uff3b-\uff3d\uff3f\uff5b\uff5d\uff5f-\uff65",
          // punctuation = new RegExp("[" + unicodePunctuationRe + "]", "g"),
          // wordSeparators = /[ \f\n\r\t\v\u1680\u180e\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u2028\u2029\u202f\u205f\u3000\u3031-\u3035\u309b\u309c\u30a0\u30fc\uff70]+/g,
          // discard = /^(@|https?:|\/\/)/,
          // htmlTags = /(<[^>]*?>|<script.*?<\/script>|<style.*?<\/style>|<head.*?><\/head>)/g,
          // matchTwitter = /^https?:\/\/([^\.]*\.)?twitter\.com/,

      var fill = d3.scale.category10(),
          minimumFontsize = 20,
          maximumFontsize = 100;

      var wholeWordsOnlyAlpha = wholeWords
        .replace(wordNumbers, '')
        .replace(punctuation, '')
        .split(' ');

      wordsObj = wordsFrequencies(wholeWordsOnlyAlpha);
      words = Object.keys(wordsObj).map(function(word) {

        //Get rid of 'stopWords'
        word = word.replace(stopWords, '');

        // if word's length is smaller 2, do not show on wordcloud
        // 500th frequency is font-size mixium
        if( word.length >= 3){
          return {text: word, size: maximumFontsize/2 * ( Math.log10(wordsObj[word]/5) )}; }
        else { return {text: "", size:0 }; }
      })//.concat([{text:"OneBigWord", size: 50}]);

      var maxSize = d3.max(words, function(d) { return d.size; });
      var minSize = d3.min(words, function(d) { return d.size; });
      var fontScale = d3.scale.linear() // scale algo which is used to map the domain to the range
        .domain([minSize, maxSize]) //set domain which will be mapped to the range values
        .range([minimumFontsize, maximumFontsize]); // set min/max font size

      function draw(words) {
        d3.select("#wordcloud").append("svg")
          .attr("width", "100%")
          // .attr("height", h)
          // .style("background-color", "#000000")
          .attr("viewBox", "0 0 "+ w + " " + h)
          .attr("preserveAspectRatio", "xMinYMin meet")
        .append("g")
          .attr("transform", "translate(" + (w/2) + "," + h/2 + ")")
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

      d3.layout.cloud()
        .size([w, h])
        .words(words)
        .padding(3)
        .rotate(function() {
          // return ~~(Math.random() * 2) * 90;
          return 0;
        })
        .font("Impact")
        .fontSize(function(d) { return fontScale(d.size) }) // the d3 scale function is used here
        .on("end", draw)
        .start();
});
