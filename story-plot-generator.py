#Python Mad Libs / beginning of story plot generator


pseudocode

variables:

Story.circle #set up how characters chase and bash into each other over 
	.internal = #wound at beginning. B plot. Set to 8 basic stages for an arc. Maybe start with set of 8 total stages for the 20 or so wounds
	.external = #what separate protag0 is facing that's separate from the start. possibly C plot. Pick 20, make 8 stages also.
	#then tag each of 1-8 below with the stages in .internal and .external, respectively. These can be second and 3rd lines after main plot.
	.0_before #what antagonist has been up to - generate a separarte storycircle for that?? And then have that feed this one
	.1_statusquo
		protag0.attributes
		location #all of them in a row, starting from the first filled status.
		protag0_0 #and so on through his helpers.
		antag #and his situation prior to story start.
		antaog0_0 #and so on through all of them
	.2_need #probably into MacGuffin, reason why protag and antag have opposing needs. 
		#there is a...
		macguffin.item 
		#that can  / has the power to
		macguffin.value
		#that the  
		macguffin.purpose
		#because it can 
		{plot A?}
		#but the protag is unsure it can help because
		{plot B?}
		#which is further complicated by 
		{plot C?}
	.3_go
		#where they go depends on:
		#1. the macguffin.purpose
		#2. the location.(subset) that fits that purpose
		# if .save		#protag wants to save and antag wants to destroy it, or vice versa
			#then location is a 3rd location, not with protag or antag
		# if .take		#protag wants to take from the antag, or vice versa 
			#then location is with person who other is attempting to take it from
		# if .destroy 	#protag wants to destroy and antag wants to save, or vice versa
			#then location is with person who other is attempting to take it from
		# if .prevent		1. #protag is trying to keep from antag, or vice versa
			#then location is with person who other is attempting to take it from
					#		2.	#protag is trying to keep from antag AND vice versa
					#then location is with person who other is attempting to take it from
		# if .location ? # have it in a different location than protag or antag, depending on which of the above?
		(Protag or antag) goes to expected location of macguffin.
		(opposing helpers) block and clash
	.4_search
		(Protag or antag) (helpers) locate macguffin or clue to its location.
		(Protag or antag) (helpers) must look for/fight to get macguffin) 
	.5_find
		(Protag or antag) (helpers) find macguffin
	.6_pay
		(Protag or antag) (helpers) fight over macguffin
		(Protag or antag) must give up something dear to get macguffin
		Internal stage here
	.7_return #this is the final clash of protag and antag.
		(protag or antag) final conflict
	.8_change 
		(protag or antag) victorious or failed

story.character
	.protag0 = main character
	.protag0_0 = 1st helper of main character
	.antag0 = main opposer of main character
	.antago0_0 = 1st helper of opposer of main character

story.character.(label).attributes
	.name
	#"is a..."
	.age #0-100, and/or also set range with a default of 18-50
	#year old
	.genetic background #white, black, Asian, East Asian, polynesian. Can weight percentages based on region.
	.orientation 	#include asexual, poly
	.sex 			#if trans, include male-identifying or female-identifying
	#with a...
	.wound #formative psychological wounding from earlier in character's life. Prob use list from character traits book. Also not vital, some action heroes have apparently no wounding such as Jack Reacher, Jack Bauer
	#and a....
		.stage #one of the 5 stages of grief, plus a 6th stage of resolution
	.desire #internal conflict separate from main conflict, providing ultimate lesson or failure. Ends up different for antag than protag (usually, maybe weighted for protag failure 1 out of 5 times)
	#(Name) is
	.economic background #keep it simpler - poor, middle class, rich
	#and works as a 
	.occupation
	#in 
	.geographic background #for earth, by continent. for fantasy, enter options?
	#(Name) is...
	.dnd_stats #strength, intelligence, wisdom, health etc.?
	#and his alignment and outlook is...
	.dnd_alignment
	#(Name) is good at
	.skill #a unique skill
	#and is (protag0's) or (antag's) (make switchable with ranodmization?)
	.relationship #the relationship to the protag or the antag. So far: (self (if protag), stranger (if no previous connection), friend, family member (series), colleague, neighbor, coworker, boss, frenemy, lover, ex-lover)
		#if the relationship is to protago or antag is "self" skip the relationship as part of the output.
		#relationship is reciprocal and affects both. 
		#good to leave room for possibility of connections with both. So a character can be protag's friend and antag's nephew, for example.
	.location #copied from story.location, as a subset of the default story level. So if the story level is set at star system, the protagonist would be at one world. If the antagonist is on a different world, it would start as a world of the same star.
	
story.genre #loads different location / setting options? also travel options?

story.location #could n.k. jemison this. Maybe have this scale to whatever level is started with? So if in solar system, planets and then continents. Or if in house, floors and then rooms.
	#location sets where characters and macguffin are, as different subsets.
	#macguffin location in particular is set as a result of macguffin purpose
	.universe #vague. A universe where magic is real. a universe where aliens have taken over the galaxy. 
			#can look at fantasy writer's world-building here? Probably a separate module.
			#set up so starts from first filled attribute downwards.
	.dimension #an alternate to universe-> world? for everything above world? 
	.galaxy
	.star system
	.world
	.region
	.country #
	.city 	#could also be city, town, village. Also nested below country.
	.place 	#house, school, hospital, shack, boat etc. 
			#prob good to have a stock bunch of types of places. Homes, barracks, etc. Perhaps aligned with character?
	.room 	#sub location or area in place
	.time 	#historical times? this is complicated to set up and would mean further work. perhaps a plug in pack
		
macguffin
	.item #literally any noun. Probably swap out for genre.
	.value #value or power. Could take input.
	.purpose 		#4 basic story options: 
		.save		#protag wants to save and antag wants to destroy it, or vice versa
		.take		#protag wants to take from the antag, or vice versa 
		.destroy 	#protag wants to destroy and antag wants to save, or vice versa
		.prevent	#protag is trying to keep from antag, or vice versa
					#protag is trying to keep from antag AND vice versa
		.location ? # have it in a different location than protag or antag, depending on which of the above?
			.clue(0),clue(1) #if macguffin isn't found at first location, a clue is found instead.
	

	
#nice to haves

input #for every listed option

genre #separated list of specific names, macguffins, nouns and verbs for:
	.romance
	.thriller
	.noir
	.scifi
	.fantasy
	
pulpy
	.skill_mod #gives antag a unique way to kill/destroy that drives the story
	.fight #insert fight or strong conflict every 1500 projected words		
	
conflict #can set for various outcomes through storyCircle. Should occur at least once in each point of StoryCircle
	.outcome #weighted towards protag losing in beginning, then either: 
		.alternating # to end with protag winning
		.semiRandom #protag loses first, random, then wins at end
		.totalRandom #each conflict is a coin flip.
		
### variable libraries / arrays below here. May split out as separate files as needed.

location_list #several different arrays as a hierarchy? Overlapping depending on choices? NK Jemison inspired / inspirated
			#universe, galaxy, solar system, planet, moon
			#hemisphere, continent or sea, region, climate
			#nation, state, city, neighborhood
			#building, floor, wing, room
			#dimension, alt reality Earth, entirely different planet (can skip straight to world, for a lot of fantasies)
			#setting: 
				#genre: (with time period as a variable?) (this may be better as sets of nouns for expansion packs? So start with one and 
					#...build out from there to others?)
					#science fiction (now, near future, past, far future, alternate history)
					#fantasy (current earth, near earth, medieval, medieval alternate earth, nothing like earth)
						#or: (magical realism, fantasy, urban fantasy, high medieval fantasy, grimdark medieval fantasy)
wound_list # each wound should also have 5 reaction stages plus a resolution
			#denial
			#anger (or fight/flight?)
			#bargaining
			#depression
			#acceptance
			#resolution			
job_nouns #		
name_nouns

	.wound #formative psychological wounding from earlier in character's life. Prob use list from character traits book. Also not vital, some action heroes have apparently no wounding such as Jack Reacher, Jack Bauer
	#and a....
		.stage #one of the 5 stages of grief, plus a 6th stage of resolution
	.desire #internal conflict separate from main conflict, providing ultimate lesson or failure. Ends up different for antag than protag (usually, maybe weighted for protag failure 1 out of 5 times)
	#(Name) is
	.economic background #keep it simpler - poor, middle class, rich
	#and works as a 
	.occupation
	#in 
	.geographic background #for earth, by continent. for fantasy, enter options?
	#(Name) is...
	.dnd_stats #strength, intelligence, wisdom, health etc.?
	#and his alignment and outlook is...
	.dnd_alignment
	#(Name) is good at
	.skill #a unique skill
	#and is (protag0's) or (antag's) (make switchable with ranodmization?)
	.relationship #the relationship to the protag or the antag. So far: (self (if protag), stranger (if no previous connection), friend, family member (series), colleague, neighbor, coworker, boss, frenemy, lover, ex-lover)
		#if the relationship is to protago or antag is "self" skip the relationship as part of the output.
		#relationship is reciprocal and affects both. 
		#good to leave room for possibility of connections with both. So a character can be protag's friend and antag's nephew, for example.
	.location 
	
	#test change