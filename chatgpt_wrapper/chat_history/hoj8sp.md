Model: GPT-4

> I have a value in and excel column for time: 00:02:00.26 I want to extract the milliseconds using a folmula such as: = "PT" & TEXT(HOUR(C2),"0#") & "H" & TEXT(MINUTE(C2),"0#") & "M" & TEXT(SECOND(C2),"0") how can I do that?
> 
> 1 / 1

To extract milliseconds from a time value like 00:02:00.26 in Excel, you can use the following formula:

less

```less
=RIGHT(TEXT(C2, "hh:mm:ss.00"), 2)
```

In your specific case, if you want to incorporate the milliseconds in your current formula, you can modify it like this:

sql

```sql
= "PT" & TEXT(HOUR(C2), "0#") & "H" & TEXT(MINUTE(C2), "0#") & "M" & TEXT(SECOND(C2), "0") & "." & RIGHT(TEXT(C2, "hh:mm:ss.00"), 2) & "S"
```

This formula will result in a value like "PT00H02M00.26S" which includes the milliseconds as well.

1 / 1