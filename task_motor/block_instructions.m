% displays brief instructions screen at the start of each block, specifying
% current block number

function block_instructions(b,window,windowRect)

% Get window center
[~,Y] = RectCenter(windowRect);

% Specify text
str1 = sprintf('You will now start block number %s.',b);

str2 = 'RED fixation: pay attention for a cue indicating which response you should make';
str3 = 'GREEN fixation: execute response as quickly as possible';
str4 = 'BLUE fixation: rest and blink if needed';

str5 = 'Keep looking at the fixation point at all times!';

str6 = 'Make a LEFT response with your left index finger';
str7 = 'Make a RIGHT response with your right index finger';

str8 = 'Press a button to begin...';

% Display text
DrawFormattedText(window,str1,'center',Y-280,[255 255 255]);

DrawFormattedText(window,str2,'center',Y-180,[255 255 255]);
DrawFormattedText(window,str3,'center',Y-140,[255 255 255]);
DrawFormattedText(window,str4,'center',Y-100,[255 255 255]);

DrawFormattedText(window,str5,'center',Y,[255 255 255]);

DrawFormattedText(window,str6,'center',Y+100,[255 255 255]);
DrawFormattedText(window,str7,'center',Y+140,[255 255 255]);

DrawFormattedText(window,str8,'center',Y+280,[255 255 255]);

Screen('Flip', window);

% Wait for response
WaitSecs(0.5);
keyIsDown = 0;
while ~keyIsDown
    [keyIsDown, ~, ~] = KbCheck;  % checking for response
end