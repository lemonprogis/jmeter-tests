// use the below to collect links from a page. 
// will filter them as well, only leaving unique links

var collectUniqueLinks = function() {
	var arr = [], l = document.links;

	for(var i=0; i<l.length; i++) {
  		arr.push(l[i].href);
	}


	var filteredLinks = arr.filter(function(item, pos) {return arr.indexOf(item) == pos;});
	// log links	
	filteredLinks.forEach(function(link){ console.log(link); });
	return filteredLinks;
};



