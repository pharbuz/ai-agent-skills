> Source: [https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-macros](https://docs.dynatrace.com/docs/platform/grail/dynatrace-pattern-language/log-processing-macros)

# DPL Pattern Expression Macros

**$$name = matcher_expr …**

A series of matcher expressions (a subpattern) can be assigned to a variable - a macro. The resulting macro expression can be used in subsequent patterns. This allows building complex patterns that are still easily readable.

#### Example

Declaring [BSD Syslog](https://tools.ietf.org/html/rfc3164#page-10) header:

```
Sep  1 02:27:01 c69-76 CRON[30297]: pam_unix(cron:session): session closed for user root
Sep  1 02:37:06 c69-76 sshd[30365]: Did not receive identification string from 197.159.170.108
Sep  1 02:39:01 c69-76 CRON[30376]: pam_env(cron:session): Unable to open env file: /etc/default/locale: No such file or directory

```

In the following pattern, line 1 declares the Syslog header subpattern (timestamp followed by hostname) and line 2 uses it in Syslog record pattern:

```
$$syslog_hdr = TIMESTAMP('MMM d HH:mm:ss'):ts ' ' LD:host;
$syslog_hdr ' ' LD:process ': ' LD:message EOL;

```

Result:tshostprocessmessage`2019-09-01 02:27:01.000 +0000``c69-76``CRON[30297]``pam_unix(cron ...``2019-09-01 02:37:06.000 +0000``c69-76``sshd[30365]``Did not receive ...``2019-09-01 02:39:01.000 +0000``c69-76``CRON[30376]``pam_env(cron: ...`

Assigning an export name to macro will result in:

1.

2.
- exposing exported subpattern expressions in a tuple structure
3.

4.
- if there are no exported subpattern expressions, then matched data is exported as string
5.
