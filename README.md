## Tintin scripts

These scripts are what I use on TinTin v 2.02.41. Some quick highlights and features as they relate to Imperium's gaming systems, from what I'd consider "standard" to a little more exotic:

1. Lots of aliases for spells and stuff like swapping gearsets
2. Gags for the most common spammy-type spells
3. Subs for some things that might be useful to always know: no_summon, levitate, int/wis gear, etc.
4. Actions for most combat-reactive stuff (although I might be missing some!)
5. XP tracker for your sessions (hint: you'll need a "main" session to #show to, eg. the character you main)
6. Tank prompts for major spells: Sanctuary, Blink, Stoneskin - should probably add more? (the default in-game prompts are a bit too simple for me)
7. Custom prompt for mages with a Mirror Image counter
8. Scroll and Potion cooldown timers (staves might not be possible)
9. Component counters (currently implemented for portal)
10. Auto-remem
11. Eqlist integration 

## Files

Most of the cool stuff is in common.tt

fr.tt (barb) has auto-track and an assess script<br>
locke.tt (mage) has the mirror-image and "tank" buff prompt tracker<br>
memgear.tt (spellcasters) has common subs to add [INT] and [WIS] to the item's description<br>
helt.tt (cleric) has a nexus gem/klein bottle counter, and will select the larger quantity for use with the portal spell

## Auto-remem

If you are a spellcaster and you run separate "mem" and "fighting" sets, the auto-remem functionality will track forgotten spells in combat ("you are not wise enough to remember X") and add them to a list. The next time you rest, you will be prompted for what spells you need to memorize that you have forgotten. Once you put your memset on, you'll be able to type "remem" and it will automatically re-memorize those spells.

You can access the list of spells anytime with #var forgotten_spells. Spells with spaces in them (eg. "magic vestment") should be properly tracked. Please raise an issue or find me in-game if there are issues with spells I have not been able to test (Piter's chain lightning, major/minor globe are a few).

## Eqlist integration

On Google Drive there is an eqlist in Sheets (Excel) which is formatted by tab with each item slot/type - light, finger, wand, shield, etc. Some of you have access, many of you may not. It is a publicly-writeable document therefore I am not going to link it here. If you need this, find me in-game, email me (see below), @me on Facebook group or Discord!

The doc is a holdover from Empire days I believe, so there are definitely items in the list that don't exist anymore (Tar Valon is one that comes to mind) but I've left them there for posterity and in case an Imm ever gets the itch to re-create from memory. Where I've taken an interest (hey, I need an upgrade in slot X), I've ported some IDs from the impeq.rtf that is also floating around. 

Ideally, these converge and we gain a single source of truth.

The current (July 2024) integration will allow you to run a piece of Python code that will convert and format a CSV properly for usage by the #SCAN CSV LINE functionality in TinTin.

In-game, formatting is critical to getting a proper match. If a match is not found, it will simply return a blank line.<br>
Syntax:<br>
id "name of object"

Example:<br>
id "a magical beam of light"<br>
Item:           a magical beam of light<br>
Type:           weapon<br>
Damage:         crit<br>
Affects:        dr+\, hr+<br>
Grants:         <br>
Location:       Soul Asylum\, soul of a high priest<br>
Other:          vorpal

In-game, this is formatted with tabular spacing, markdown doesn't do a great job here :) 

You'll also notice the un-escaped commas, which are difficult to deal with in a comma-separated file. Right now it's a minor nuisance so I'll get around to optimizing in the future (see TODO). 

### TODO:
1. Group / room report
2. Format the list so that a direct download is all that should be necessary
3. Integrate an auto-download of the latest eqlist at session start
4. Write in-game functionality (via TinTin, not the mud codebase) to add identified (via the spell) items to the database
5. Add affect1/affect2 dedicated columns to ease parsing

## Feedback

As always reach out to me if you have any questions on how things work, want to customize for a class I don't play, etc.

## Squad

Helt (cleric)
Feydrautha (barb)
Locke (mage)
Petra (thief)
Amergin (druid)

[kgarreau@gmail.com](mailto:kgarreau@gmail.com)