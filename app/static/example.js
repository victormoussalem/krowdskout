d3.json("history.json", function(json) {

	if (json === null) return; // parse problem, nothing to do here

	// setup data for chart
	
	json.events.forEach(function(p, i) {
		var mom = moment(p.published_at).format('MMMM Do YYYY, h:mm:ss a');
		console.log(mom);
		p.published_at = mom; // coerce into right type
	});

	json.events.sort(function(a,b) { return a.published_at < b.published_at ? -1 : a.published_at > b.published_at ? 1 : 0; });

	// instantiate the chart

	var chart = timelineChart(); 
	
	chart.title(function(d) { return d.device; })	// accessor for event title
		 .date(function(d) { return d.published_at; })	// accessor for event date
		 .details(function(d) {
	//	 return d.data; })
		 if (d.data < 0)
			return (-1) * d.data + " people walked out";
		else if (d.data == 1)
			return d.data + " person walked in";
		else if (d.data == -1)
			return (-1) * d.data + " person walked out";
		else
			return d.data + " people walked in";
		})
		 .width(600);							// width of chart

	// join and render

	d3.select("#chart").datum(json.events).call(chart);
});
