# Compute each channel's share of resolved tickets using its own denominator.
args <- commandArgs(trailingOnly = TRUE)
path <- if (length(args)) args[[1]] else "Comcast Telecom Complaints data.csv"
tickets <- read.csv(path)
statuses <- trimws(tickets$Status)
channels <- trimws(tickets$Received.Via)
stopifnot(all(statuses %in% c("Closed", "Solved", "Open", "Pending")))
stopifnot(!anyNA(channels), all(nzchar(channels)))
resolved <- statuses %in% c("Closed", "Solved")
totals <- table(channels)
resolved_counts <- tapply(as.integer(resolved), channels, sum)
summary <- data.frame(
  channel = names(totals),
  resolved = as.integer(resolved_counts[names(totals)]),
  total = as.integer(totals)
)
summary$resolution_rate <- summary$resolved / summary$total
print(summary, row.names = FALSE)
