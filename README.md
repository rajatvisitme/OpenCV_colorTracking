<h1><center>OpenCV_colorTracking</center></h1>
<h2>Overview<h2>
In this module we will create a real-time color tracker using OpenCV library.<br>
    We will capture the live video using camera and then use trackbars to set color ranges, BGR respectively.<br>
    And then we will mask all the regions of live-video-feed which doesn't lies in the selected range.
<h2>Dependencies<h2>
<p><ul>
    <li>OpenCV</li>
    <li>Numpy</li>
</ul></p>
<p>Use <b>pip</b> to install any missing dependencies.</p>
    
<h2>Code-Walkthrough</h2>
<ol>
<li>Importing required libraries.</li>
<li>Creating Window and Capturing Live Video using camera.</li>
<li>Setting range values(Lower and Higher) of BGR.</li>
<li>Masking (regions not in selected range)</li>
<li>Output - Masked live video - tracking color</li>
<li>Destroying/Terminating all windows and releasing camera.</li>
</ol>
