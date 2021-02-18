
// Reference for data from js
var tableData = data;

// Reference for table body
var table = d3.select('tbody');

// Iterate over data
tableData.forEach((ufo_sightings)   =>{
    // Reference row
    var row = table.append('tr');   
    // Iterate over all key/values in an object
    Object.entries(ufo_sightings).forEach(([key,value]) => {
        // Reference data
        var data = row.append('td');
        // Input data value
        data.text(value);
    });
});

// Create a function to retrieve data based on input date and display
function buttonClick(){
   // Value property of the input element 
    var date = d3.select('#datetime').property('value');
    // Reference Filter Data
    var filterData = tableData;
    // IF statement to cross reference input date against data date
    if (date != "") {   
        filterData = filterData.filter(row => row.datetime === date)
  
    };
    
    // Remove any children from the list
        table.html('');
    // Repopulating data
        filterData.forEach((ufo_sightings)   =>{
            var row = table.append('tr');
            Object.entries(ufo_sightings).forEach(([key,value]) => {
                var data = row.append('td');
                data.text(value);
        });
        console.log(filterData)
    });
}
// Run Function when Filter Table button is clicked
d3.selectAll('#filter-btn').on('click', buttonClick); 