// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");
var submit = d3.select("#filter-btn");
tableData.forEach(function(ufoSearch) {
    console.log(ufoSearch);
    var row = tbody.append("tr");
    Object.entries(ufoSearch).forEach(function([key, value]) {
      console.log(key, value);
      var cell = row.append("td");
      cell.text(value);
    });
  });

console.log(tableData);
submit.on("click", function() {
    d3.event.preventDefault();
    var inputElement = d3.select("#datetime");
    var inputValue = inputElement.property("value");
    console.log(inputValue);
    var filteredData = tableData.filter(sight => sight.datetime === inputValue);
    console.log(filteredData);
    var tbody = d3.select("#tbody-alien").text("")
    filteredData.forEach(function(ufoPull) {
        console.log(ufoPull);
        var row = tbody.append("tr");
        Object.entries(ufoPull).forEach(function([key, value]) {
          console.log(key, value);
          var cell = row.append("td");
          cell.text(value);
        });
      });
});



