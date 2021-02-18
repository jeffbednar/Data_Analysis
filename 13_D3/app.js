var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 80,
  left: 100
  };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3
  .select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

d3.csv("data.csv").then(function(censusData) {

  console.log(censusData);
   
    // parse data
    censusData.forEach(function(data) {
      data.smokes = +data.smokes;
      data.age = +data.age;
    });

    var xLinearScale = d3.scaleLinear()
      .domain(d3.extent(censusData, d => d.age))
      .range([0, width]);
    
    var yLinearScale = d3.scaleLinear()
      .domain([0, d3.max(censusData, d => d.smokes)])
      .range([height, 0]);

    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    var xAxis = chartGroup.append("g")
      .classed("x-axis", true)
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    var toolTip = d3.tip()
      .attr("class", "d3-tip")  
      .html(d => 
        `<strong><h4>${d.state}<strong></h4><hr><h5>Age:<br>${d.age}<br>% of Smokers:<br>${d.smokes}</h5>`);
      

  
    var circlesGroup = chartGroup.selectAll("circle")
    .data(censusData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.age))
    .attr("cy", d => yLinearScale(d.smokes))
    .attr("r", 10)
    .attr("fill", "blue")
    .attr("opacity", ".5")
    .on("mouseover", toolTip.show)
    .on("mouseout", toolTip.hide);

    chartGroup.selectAll("text.text-circles")
    .data(censusData)
    .enter()
    .append("text")
    .attr("x", d => xLinearScale(d.age))
    .attr("y", d => yLinearScale(d.smokes))
    .text(d => d.abbr)
    .attr("text-anchor", "middle")
    .attr("alignment-baseline", "central")
    .attr("fill", "white")
    .attr("font-size", "12px")
    .style("font-weight", "bold")

    circlesGroup.call(toolTip);

    var labelsGroup = chartGroup.append("g")
    .attr("transform", `translate(${width / 2}, ${height + 20})`);

  var ageLabel = labelsGroup.append("text")
    .attr("x", 0)
    .attr("y", 20)
    .attr("value", "age") // value to grab for event listener
    .classed("active", true)
    .text("Median Age")

  // append y axis
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .classed("axis-text", true)
    .text("% of Smokers");

  }) 


.catch(function(error) {
    console.log(error);
  });
  