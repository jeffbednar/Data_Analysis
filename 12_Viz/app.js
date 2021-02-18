  const file = "samples.json";
function buildCharts(samplechoice) {
    d3.json(file).then((data) => {
        var sample = data.samples.filter(a => a.id==samplechoice);
        var sampleotuids = sample[0].otu_ids;
        var samplevalues = sample[0].sample_values;
        var samplelabels = sample[0].otu_labels;
        var yvalues = sampleotuids.slice(0,10).reverse().map(id => `OTU ${id}`);
        console.log(samplelabels)
        var trace = [{
            type: 'bar',
            x: samplevalues.slice(0,10).reverse(),
            y: yvalues,
            orientation: 'h'
          }];

        var layout = {
          margin: {t:25, l:100},
        }

        Plotly.newPlot('bar', trace, layout);

        var trace1 = [{
            x: sampleotuids, 
            y: samplevalues,
            text: samplelabels,
            mode: 'markers',
            marker: {
              size: samplevalues,
              color: sampleotuids,
              colorscale: "Earth",
              text: samplelabels,
            }
          }];
          var layout1 = {
            title: 'Marker Size',
            showlegend: false,
            height: 600,
            width: 1200,
            xaxis:{title: "OTU ID"},
          };
        Plotly.newPlot('bubble', trace1, layout1);
    })    
}
function meta(samplechoice) {
    d3.json(file).then((data) => {
        var metadata = data.metadata.filter(metadata => metadata.id==samplechoice)
        var populator = d3.select("#sample-metadata")
        populator.html('');
        populator.append('h5').text(`id: ${metadata[0].id}`);
        populator.append('h5').text(`ethnicity: ${metadata[0].ethnicity}`);
        populator.append('h5').text(`gender: ${metadata[0].gender}`);
        populator.append('h5').text(`age: ${metadata[0].age}`);
        populator.append('h5').text(`location: ${metadata[0].location}`);
        populator.append('h5').text(`bbtype: ${metadata[0].bbtype}`);
        populator.append('h5').text(`wfreq: ${metadata[0].wfreq}`);
    }) 
}
function optionChanged(samplechoice) {
    buildCharts(samplechoice);
    meta(samplechoice);
}

function init() {
    d3.json(file).then((data) => {
        var selector = d3.select("#selDataset");
        data.names.forEach(element => {
            selector.append("option").text(element).property("value", element);
        });
    })
    buildCharts(940);
    meta(940);
}
init();