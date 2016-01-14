library("jsonlite")
library(RgoogleMaps)
library(ggplot2)
library(ggmap)


url <- "http://opendata.iprpraha.cz/CUR/FSV/FSV_VerejnaWC_b/WGS_84/FSV_VerejnaWC_b.json"
download.file(url, "data.json")

document <- fromJSON(url)


df = data.frame(matrix(vector(), length(document$features$geometry$coordinates), 2,
                       dimnames=list(c(), c("Lat", "Long"))),
                stringsAsFactors=F)

lats = numeric()
longs = numeric()


for (number in 1:length(document$features$geometry$coordinates)){
      pair <-  as.vector(document$features$geometry$coordinates[number][[1]])
      
      lats <- append(lats,as.numeric(pair[2]))
      longs <- append(longs,as.numeric(pair[1]))

}

df$Lat <- lats
df$Long <- longs




WCmap <- get_map(location = c(mean(df$Long),mean(df$Lat)), zoom = 12, maptype = "watercolor", scale = 4)

# plotting the map with some points on it
ggmap(WCmap) +
      geom_point(data = df, aes(x = Long, y = Lat, fill = "red", alpha = 0.8), size = 5, shape = 21) +
      guides(fill=FALSE, alpha=FALSE, size=FALSE)
