# Known Issues

Here's a list of issues we know about, that you may be experiencing.

### 100% CPU spikes

This affects:

* Single-core machines \(&gt;10 years old\)
* Running Windows 7 or Windows Server 2012

If you have this combination, you'll see excessive \(near-100%, not just 10-15%\) CPU usage throughout. A possible workaround is to manually set the process's priority to "Below Normal":

* Open the Task Manager \(Shift+Ctrl+Esc\)
* Switch to the "Details" tab
  * You might need to click "More details" to expand the Task Manager first, if it's your first time using it
* Find "itch.exe" in the list
  * You can click the list and start typing "itc" to focus it
  * You can also sort by Name by clicking the "Name" column so processes jump around less
* In the context menu \(Right-click on "itch.exe"\)
  * Select "Set priority" =&gt; "Below Normal"

This issue _sucks_. We're just as angry as you are. Maybe one day we'll switch to something else or ship an alternative, minimalist client - until then, the workaround will have to do.

