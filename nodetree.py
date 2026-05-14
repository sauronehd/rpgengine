# AUTO-GENERATED from thestorynew.excalidraw
# Keywords have been pre-filled based on story context.
from nodeClass import *
from pinCalls import *


class nodeTree:

    # ── NODE DEFINITIONS ─────────────────────────────────────────
    beginning = outputNode()
    beginning.prompt = ("You wake up in a strange, filthy room with stone walls and dim lighting. It's "
        "blisteringly hot and somehow, you know you're in hell. You see a stone door at "
        "one end of the room, and a small vent on the other end. Inspect the vent or open "
        "the door")
    beginning.outputs = [
        [pins.heat, pinState.on],
    ]

    push_open_large = outputNode()
    push_open_large.prompt = ("You push open the large stone door. It grinds open slowly with a painful noise. "
        "When outside, you see a dimly lit hallway, extending left and right. as you "
        "decide where to go, you feel a slight rumbling in the floor, though you don't "
        "know why. Go left or go right")
    push_open_large.outputs = [
        [pins.speaker, pinState.on],
        [pins.subwoofer, pinState.on],
    ]

    inspect_vent_air = outputNode()
    inspect_vent_air.prompt = ("You inspect the vent. Air blows through it, feeling thick on your face. You pull "
        "off the cover with ease, finding it barely attached by rusty screws. inside you "
        "see a small skeleton clutching an object wrapped in cloth. You pull it out and "
        "unwrap it, finding a simple dagger. you pocket it and leave.")
    inspect_vent_air.outputs = [
        [pins.heat, pinState.on],
        [pins.fan, pinState.on],
    ]

    imp_wasnt_found = outputNode()
    imp_wasnt_found.prompt = ("IF THE IMP WASN'T FOUND: You go left down the hall, and find another door with "
        "light shining through, and a small out-cove just large enough to fit in, broken "
        "into the wall. You hear something approaching rapidly. Run through the door or "
        "hide in the alcove")
    imp_wasnt_found.outputs = [
        [pins.speaker, pinState.on],
        [pins.heat, pinState.on],
    ]

    move_down_hall = outputNode()
    move_down_hall.prompt = ("you move down the hall, soon finding another room. In it you see a grotesque, "
        "impish creature, and it sees you. It's clearly a threat. Try to kill it or turn "
        "and run")
    move_down_hall.outputs = []

    have_dagger_lunge = outputNode()
    have_dagger_lunge.prompt = ("IF YOU HAVE THE DAGGER: You lunge forwards and plunge the the dagger you found "
        "mere moments ago into its throat. it lets out a gargled cry and falls limp. You "
        "see a large door just past it and a deep rumbling comes from it. Open the door "
        "or turn and walk away.")
    have_dagger_lunge.outputs = [
        [pins.subwoofer, pinState.on],
        [pins.speaker, pinState.on],
    ]

    dont_have_dagger = outputNode()
    dont_have_dagger.prompt = ("IF YOU DONT HAVE THE DAGGER: You jump on the creature and try to strangle it, "
        "but its vicious and deadly. After a short struggle it slashes you with its sharp "
        "claws and you fall dead, your last sight being the creature laughing as it "
        "watches the life leave your eyes. END")
    dont_have_dagger.outputs = [
        [pins.speaker, pinState.on],
    ]

    walk_back_way = outputNode()
    walk_back_way.prompt = ("You walk back the way you came, and go past the door you first came from. You "
        "find another door with a light shining through. You step through it and find "
        "yourself blinded by a inferno in the form of a lake of fire. As your eyes adjust "
        "you see a large rock wall to your right and a path leading down straight ahead "
        "of you")
    walk_back_way.outputs = [
        [pins.heat, pinState.on],
    ]

    rush_back_way = outputNode()
    rush_back_way.prompt = ("You rush back the way you came, past the door you first exited and find another "
        "door, this one with a light shining through. You also notice an alcove you could "
        "hide in. The creature is close behind.")
    rush_back_way.outputs = [
        [pins.heat, pinState.on],
    ]

    hide_alcove_see = outputNode()
    hide_alcove_see.prompt = ("You hide in the alcove and see the legs of a strange, hellish creature. You hold "
        "your breath for what feels like an eternity, but the creature turns and walks "
        "away. you wait a second longer and then leave your hiding place. Go through the "
        "door with light shining through or follow the creature.")
    hide_alcove_see.outputs = []

    run_through_door = outputNode()
    run_through_door.prompt = ("As you run through the door the steps of the creature behind you speed up and "
        "you hear it let out a screech, which you quickly realize was an alarm when "
        "another set of footsteps start pounding after you, each footfall shaking the "
        "very foundations of the world. You are momentarily blinded by a blazing inferno, "
        "but keep running straight ahead. As you run you see a fork in the path your on. "
        "Go right or go left.")
    run_through_door.outputs = [
        [pins.subwoofer, pinState.on],
        [pins.speaker, pinState.on],
    ]

    try_hide_but = outputNode()
    try_hide_but.prompt = ("You try to hide but the creature was too close behind you. It drags you out by "
        "your feet and mauls you with its sharp claws and teeth, killing you quickly and "
        "painfully. END")
    try_hide_but.outputs = []

    climb_rock_wall = outputNode()
    climb_rock_wall.prompt = ("You climb the rock wall, nearly falling at multiple points but ultimately "
        "getting to the top. There you find the entrance to a cave. You step into it and "
        "find your way through. With each step the once blistering heat cools down to "
        "near freezing. As you press forward you eventually see a light ahead. It's "
        "another mouth to this cave, and you see snow blowing in through it. You continue "
        "through the entrance, eventually being met by a frozen wasteland. Directly "
        "In front of you is a pack of unnatural, wolf like creatures feasting on the "
        "corpse of a man about your size. As they see you they scatter out of sight, but "
        "you feel like they are still watching you. Inspect the corpse or start "
        "exploring.")
    climb_rock_wall.outputs = [
        [pins.fan, pinState.on],
        [pins.cold, pinState.on],
    ]

    only_open_door = outputNode()
    only_open_door.prompt = ("You only open the door a crack when a force sends you flying back against a "
        "wall. You see a massive quadrupedal beast with sharp horns and spikes, long "
        "tongues which protrude from its mouth, and razor sharp teeth with 6 eyes just "
        "above. It stops to roar, and you try to run, but the force imparted on your body "
        "from hitting the wall leaves you injured. Your sides light up with pain as you "
        "move, and you aren't even able to regain your balance before the beast closes "
        "the gap and eats you alive in a gruesome scene. END")
    only_open_door.outputs = [
        [pins.speaker, pinState.on],
    ]

    walk_down_path = outputNode()
    walk_down_path.prompt = ("As you walk down the path its not long before you find a fork in the road. the "
        "path to the right seems to be a winding road around the rock face you just saw. "
        "to your left is a much shorter path which seems to lead to the bank of the lake "
        "of fire.")
    walk_down_path.outputs = [
        [pins.heat, pinState.on],
    ]

    run_right_find = outputNode()
    run_right_find.prompt = ("You run to the right, and find yourself on a winding road going up the side of a "
        "cliff. You can hear the imp close on your tail, and catch glimpses of the second "
        "creature, a massive horror. Luckily for you it seems too large for the path and "
        "slows down as it climbs the cliff, giving you a little extra space. You keep "
        "sprinting, your legs begin to burn and your lungs feel like they will pop but "
        "you refuse to die. Eventually you find your way to a cave and you go in, giving "
        "your last push of strength in a desperate attempt to live. Eventually you lose "
        "them, and find a way out. You exit the cave, finding yourself in a frozen "
        "wasteland, the frigid winds a stark contrast to the blistering heat you came "
        "from. Looking around as you catch your breath you hear the scattering of many "
        "creatures, catching a glimpse of a tail. You feel like your being watched. In "
        "front of you is a corpse. Inspect the corpse or start exploring.")
    run_right_find.outputs = [
        [pins.speaker, pinState.on],
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    turn_left_keep = outputNode()
    turn_left_keep.prompt = ("You turn left and keep running, both creatures hot on your tail, the thundering "
        "footsteps sending vibrations through your body. As you run you quickly find "
        "yourself on the bank of a lake of fire. You go along its edge in your continued "
        "attempt to survive, but your pant legs catch on fire. Shocked and panicked you "
        "fall, rolling around, trying to put out the fire and escape your pursuers. The "
        "fire spreads up your clothing, and you see the monstrosities behind you slow as "
        "you writhe on the ground, still coming none the less. You see a nearby overhang "
        "of earth, only a few feet away that you could potentially crawl into to safety. "
        "The thought to play dead also occurs to you.")
    turn_left_keep.outputs = [
        [pins.speaker, pinState.on],
        [pins.subwoofer, pinState.on],
        [pins.heat, pinState.on],
    ]

    play_dead_hoping = outputNode()
    play_dead_hoping.prompt = ("You play dead, hoping they will think you burned to death, but its quickly "
        "apparent that this was a bad idea. The fire spreads further and it becomes "
        "impossible to hold in your cries of pain. As the monsters on your tail catch up "
        "to you, they dont do anything, instead watching as you burn and relishing in "
        "your agony. You sought to play dead in hopes of living, and yet the act you put "
        "on became a reality. END")
    play_dead_hoping.outputs = [
        [pins.heat, pinState.on],
        [pins.speaker, pinState.on],
    ]

    crawl_under_overhang = outputNode()
    crawl_under_overhang.prompt = ("You crawl under the overhang, making sure to throw as much ash and dust on your "
        "body as possible as you go to put out the fire. In seconds that feel like hours "
        "you get as far in the overpass as physically possible, and find that it isn't "
        "nearly deep enough to protect you. The hell spawn trying to kill you are now "
        "close enough to touch and you freeze in fear as the imps long claws poke your "
        "leg. You prepare yourself for the end that never comes. After several minutes "
        "you finally move. You have bad burns but are no longer on fire. Additionally the "
        "demons are no longer in sight. You assume they thought you crawled in there to "
        "die and left your corpse to rot. You breath a sigh of relief and look around. In "
        "the overhang your in, you see a stone that radiates warmth, much more soothing "
        "than that of the heat provided by the fires all around. You take it and go back "
        "then way you came in safety, moving cautiously regardless. Eventually you find "
        "the fork in the road and go the other way.")
    crawl_under_overhang.outputs = [
        [pins.heat, pinState.on],
    ]

    walk_up_best_1 = outputNode()
    walk_up_best_1.prompt = ("Your walk up is best described as uneventful, a pleasant change of pace. You "
        "eventually get to the end of the road. There you find the entrance to a cave. "
        "You step into it and find your way through. With each step the once blistering "
        "heat cools down to near freezing. As you press forward you eventually see a "
        "light ahead. It's an exit to this cave, and you see snow blowing in through it. "
        "You continue through the entrance and are met by a frozen wasteland. Directly In "
        "front of you is a pack of unnatural, wolf like creatures feasting on the corpse "
        "of a man about your size. As they see you they scatter out of sight, but you "
        "feel like they are still watching you. Inspect the corpse or start exploring.")
    walk_up_best_1.outputs = [
        [pins.fan, pinState.on],
        [pins.cold, pinState.on],
    ]

    go_left_towards = outputNode()
    go_left_towards.prompt = ("You go left, towards the lake of fire. The closer you get to the shore the more "
        "painful the heat is. Nevertheless you walk along the shore for awhile until "
        "finding a small overhang of earth. You decide to look under it and find a small "
        "stone that seems to radiate a soothing warmth, easily discernible from the blaze "
        "around you. You take it and keep walking. Finding nothing else of interest you "
        "turn back, feeling that going this way wont get you anywhere. Retracing your "
        "steps to the fork in the road and taking the other path")
    go_left_towards.outputs = [
        [pins.heat, pinState.on],
    ]

    kneeling_down_inspect_1 = outputNode()
    kneeling_down_inspect_1.prompt = ("kneeling down to inspect the corpse you find nothing of note on the mans body, "
        "but you do notice a trail of faint footprints. Deciding to follow them you find "
        "one of the creatures you saw earlier with a spear through its neck. It's fur is "
        "thick and its hide tough. Additionally it seems to have no blood. You realize "
        "that you could likely fashion a crude coat from its pelt using your dagger. "
        "Motivated by the icy winds that feel like they are cutting into your flesh, you "
        "decide to do just that. After about an hour of work the pelt is draped over you "
        "shoulders and you feel much warmer. You begin to walk, exploring your "
        "surroundings but find nothing of note. Eventually, despite there being no "
        "visible light source in the sky, it begins to darken. You see a snow bank that "
        "you think you could make a small shelter for the night in. Press forward or stop "
        "to make shelter.")
    kneeling_down_inspect_1.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    ignore_corpse_begin_1 = outputNode()
    ignore_corpse_begin_1.prompt = ("You ignore the corpse and begin to walk. Strong gusts of icy wind feel like they "
        "cut into your flesh, but you press on regardless. Wandering for hours it begins "
        "to get dark, bringing the already freezing temperatures even lower. You think to "
        "try and make a shelter but you collapse from cold and exhaustion before you can. "
        "you curl up into the fetal position and pray for a miracle, but none comes. You "
        "slowly freeze to death in the endless fields of ice and snow. END")
    ignore_corpse_begin_1.outputs = [
        [pins.fan, pinState.on],
        [pins.cold, pinState.on],
    ]

    start_explore_picking = outputNode()
    start_explore_picking.prompt = ("You start to explore, picking a direction and walking. The icy gusts of wind "
        "feel like they are cutting into your flesh with each step. despite the "
        "uncomfortable conditions you press on for hours. Before long, despite no "
        "discernible light source to go out, it gets darker, and the already freezing "
        "temperatures drop. You need shelter. unfortunately for you, none is in sight. A "
        "panic sets in as you search to no avail, your thinking impaired by the cold and "
        "exhaustion. Before light returns to the world, you slow, fall, and curl up. "
        "praying for a miracle that never comes you freeze on the endless wasteland of "
        "ice and snow. END")
    start_explore_picking.outputs = [
        [pins.fan, pinState.on],
        [pins.cold, pinState.on],
    ]

    kneeling_down_inspect_2 = outputNode()
    kneeling_down_inspect_2.prompt = ("kneeling down to inspect the corpse you find nothing of note on the mans body, "
        "but you do notice a trail of faint footprints. Deciding to follow them, you find "
        "an unnatural, wolf like creature with a spear through its neck. As you inspect "
        "the scene you hear growling all around you, and moments later you see a pack of "
        "the same creatures. They are clearly not friendly. You see a small gap in their "
        "circle and think about running. You also think about pulling the spear from the "
        "dead creatures beside you to defend yourself.")
    kneeling_down_inspect_2.outputs = [
        [pins.speaker, pinState.on],
        [pins.cold, pinState.on],
    ]

    walk_up_best_2 = outputNode()
    walk_up_best_2.prompt = ("Your walk up is best described as uneventful, a pleasant change of pace. You "
        "eventually get to the end of the road. There you find the entrance to a cave. "
        "You step into it and find your way through. With each step the once blistering "
        "heat cools down to near freezing. As you press forward you eventually see a "
        "light ahead. It's an exit to this cave, and you see snow blowing in through it. "
        "You continue through and are met by a frozen wasteland. Directly in front of you "
        "is a pack of unnatural, wolf like creatures feasting on the corpse of a man "
        "about your size. As they see you they scatter out of sight, but you feel like "
        "they are still watching you. Inspect the corpse or start exploring.")
    walk_up_best_2.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    walk_up_best_3 = outputNode()
    walk_up_best_3.prompt = ("Your walk up is best described as uneventful, a pleasant change of pace allowing "
        "you to calm your nerves. You eventually get to the end of the road. There you "
        "find the entrance to a cave. You step into it and find your way through. With "
        "each step the once blistering heat cools down to near freezing. As you press "
        "forward you eventually see a light ahead. It's another mouth to this cave, and "
        "you see snow blowing in through it. You continue through the entrance and are "
        "met by a frozen wasteland. Directly In front of you is a pack of unnatural, wolf "
        "like creatures feasting on the corpse of a man about your size. As they see you "
        "they scatter out of sight, but you feel like they are still watching you. "
        "Inspect the corpse or start exploring.")
    walk_up_best_3.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    kneeling_down_inspect_3 = outputNode()
    kneeling_down_inspect_3.prompt = ("kneeling down to inspect the corpse you find nothing of note on the mans body, "
        "but you do notice a trail of faint footprints. You decide to follow and find one "
        "of the creatures you saw earlier with a spear through its neck. It's fur is "
        "thick and its hide tough. Additionally it seems to have no blood. you realize "
        "that you can most likely fashion a crude coat from its pelt using your dagger. "
        "Motivated by the icy winds, you decide to do just that. After about an hour of "
        "work the pelt is draped over you shoulders and you feel much warmer. You begin "
        "to walk, exploring your surroundings but find nothing of note. Eventually, "
        "despite there being no visible light source in the sky, it begins to darken. You "
        "see a snow bank that you think you could make a small shelter for the night in. "
        "Press forward or stop to make shelter.")
    kneeling_down_inspect_3.outputs = []

    ignore_corpse_begin_2 = outputNode()
    ignore_corpse_begin_2.prompt = ("You ignore the corpse and begin to walk. Strong gusts of icy wind feel like they "
        "cut into your flesh, but you press on regardless. Wandering for hours it begins "
        "to get dark, bringing the already freezing temperatures even lower. You think to "
        "try and make a shelter but you collapse from cold and exhaustion before you can. "
        "you curl up into the fetal position and pray for a miracle, but none comes. You "
        "slowly freeze to death in the endless fields of ice and snow. END")
    ignore_corpse_begin_2.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    kneeling_down_inspect_4 = outputNode()
    kneeling_down_inspect_4.prompt = ("kneeling down to inspect the corpse you find nothing of note on the mans body, "
        "but you do notice a trail of faint footprints. Deciding to follow them you find "
        "one of the creatures you saw earlier with a spear through its neck. Nothing else "
        "is of note. As you stand here, you realize that the stone in your pocket is "
        "keeping you warm despite the freezing temperatures. You begin to walk, exploring "
        "your surroundings but finding nothing of note. Eventually, despite there being "
        "no visible light source in the sky to go out, it begins to darken. You see a "
        "snow bank that you think you could make into a small shelter for the night. "
        "Press forward or stop to make shelter.")
    kneeling_down_inspect_4.outputs = [
        [pins.fan, pinState.on],
        [pins.cold, pinState.on],
    ]

    ignore_corpse_pick_1 = outputNode()
    ignore_corpse_pick_1.prompt = ("You ignore the corpse and pick a direction, beginning to walk. Icy winds batter "
        "against you, but you quickly warm back up to a comfortable state after each "
        "gust. You realize you have the stone to thank for that. After several hours of "
        "walking the world around you darkens, despite there being no discernible light "
        "source to go out in the first place. Along with the darkness is a sharp drop in "
        "temperature, that even begins to overpower the comfort of the stone. You see a "
        "snow bank nearby that you could make into a small shelter for the night. Stop to "
        "make shelter or press on.")
    ignore_corpse_pick_1.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    kneeling_down_inspect_5 = outputNode()
    kneeling_down_inspect_5.prompt = ("kneeling down to inspect the corpse you find nothing of note on the mans body, "
        "but you do notice a trail of faint footprints. Deciding to follow them, you find "
        "one of the creatures you saw earlier with a spear through its neck. As you "
        "inspect the scene you hear growling all around you, and moments later you see a "
        "pack of the same creatures. They are clearly not friendly. You see a small gap "
        "in their circle and think about running. You also think about pulling the spear "
        "from the dead creature beside you to defend yourself.")
    kneeling_down_inspect_5.outputs = [
        [pins.cold, pinState.on],
        [pins.speaker, pinState.on],
    ]

    ignore_corpse_pick_2 = outputNode()
    ignore_corpse_pick_2.prompt = ("You ignore the corpse and pick a direction, beginning to walk. Icy winds batter "
        "against you, but you quickly warm back up to a comfortable state after each "
        "gust. You realize you have the stone to thank for that. After several hours of "
        "walking the world around you darkens, despite there being no discernible light "
        "source to go out in the first place. Along with the darkness is a sharp drop in "
        "temperature, that even begins to overpower the comfort of the stone. You see a "
        "snow bank nearby that you could make into a small shelter for the night. Stop to "
        "make shelter or press on.")
    ignore_corpse_pick_2.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
        [pins.heat, pinState.on],
    ]

    break_into_sprint_1 = outputNode()
    break_into_sprint_1.prompt = ("You break into a sprint, running for the gap. You make it through but only make "
        "a few steps more before you feel a nip at your heel. Looking back you see they "
        "are all chasing you, close behind and in a new formation, blocking your escape "
        "from every direction except directly ahead. You keep running, harder now but the "
        "nipping at your heels continues until eventually their teeth sink cleanly into "
        "the back of your leg. You tumble to the ground, and in moments they all descend "
        "upon you, tearing into your flesh. You die, becoming a feast for the unholy "
        "beasts. END")
    break_into_sprint_1.outputs = [
        [pins.speaker, pinState.on],
    ]

    tear_spear_out = outputNode()
    tear_spear_out.prompt = ("You tear the spear out of the creatures neck and present the point to the "
        "nearest threat. They all enclose around you but stay just out of range of your "
        "spear. You make yourself large and loud, trying to stab at them every time one "
        "tries to get close. eventually, one of your thrusts makes contact, not killing "
        "the creature but drawing blood. It pulls back and the others stay in their "
        "place. As the standoff continues they try to nip at you heels, growl, and "
        "generally intimidate you into running. Despite their attempts you stand your "
        "ground, and after landing another strike, this one sinking into the victims "
        "flesh and killing it, the rest turn and run. You breath a sigh of relief and "
        "pull the spear back out. as you do you find the haft damaged, making you "
        "hesitant to use it as a weapon again. However, as the adrenaline wears off and "
        "the cold begins to chill you down to the bones once more. You break the tip off "
        "the spear to use it like a makeshift knife and skin one of the dead creatures, "
        "turning its pelt into a very crude cloak, insulating you from the elements. You "
        "begin to walk, exploring your surroundings but finding nothing of note. "
        "Eventually, despite there being no visible light source in the sky to go out, it "
        "begins to darken. You see a snow bank that you think you could make into a small "
        "shelter for the night. Press forward or stop to make shelter.")
    tear_spear_out.outputs = [
        [pins.speaker, pinState.on],
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    tear_spear_from = outputNode()
    tear_spear_from.prompt = ("You tear the spear from the creatures neck and present the point to the nearest "
        "threat. They enclose around you but stay just out of range of your spear. You "
        "make yourself large and loud, trying to stab at them every time one gets close. "
        "eventually, one of your thrusts makes contact, not killing the creature but "
        "drawing blood. It pulls back and the others stay in their place. The standoff "
        "continues, they try to nip at your heels, growl, and generally intimidate you "
        "into running. Despite their attempts you stand your ground. After landing "
        "another strike, this one sinking into the victims flesh and killing it, the rest "
        "turn and run. You breath a sigh of relief and pull the spear out. As you do you "
        "find the haft damaged, making you hesitant to use it as a weapon again, and as "
        "such you discard it. as the adrenaline wears off you notice the freezing gusts "
        "of wind, but you also notice that you quickly warm up to a comfortable "
        "temperature afterwards. It occurs to you that you have the stone to thank for "
        "that. You begin to walk, exploring your surroundings but finding nothing of "
        "note. Eventually, despite there being no visible light source in the sky to go "
        "out, it begins to darken. You see a snow bank that you think you could make into "
        "a small shelter for the night. Press forward or stop to make shelter.")
    tear_spear_from.outputs = [
        [pins.speaker, pinState.on],
        [pins.fan, pinState.on],
    ]

    break_into_sprint_2 = outputNode()
    break_into_sprint_2.prompt = ("You break into a sprint, running for the gap. You make it through but only make "
        "a few steps more before you feel a nip at your heel. Looking back you see they "
        "are all chasing you, close behind and in a new formation, blocking your escape "
        "from every direction except directly ahead. You keep running, harder now but the "
        "nipping at your heels continues until eventually their teeth sink cleanly into "
        "the back of your leg. You tumble to the ground, and in moments they all descend "
        "upon you, tearing into your flesh. You die, becoming a feast for the unholy "
        "beasts. END")
    break_into_sprint_2.outputs = [
        [pins.speaker, pinState.on],
    ]

    stop_make_shelter_1 = outputNode()
    stop_make_shelter_1.prompt = ("You stop to make a shelter, digging a small snow-fort out of the snow bank, "
        "barely large enough to fit you inside. As you crawl in you find it plenty warm "
        "to keep you alive, but a constant dead of it collapsing on you gnaws at your "
        "mind. Despite this, you have no better option, and eventually fall asleep. You "
        "wake up with fresh light shining in the entrance. You crawl out, happy to still "
        "be alive and keep exploring. eventually, you spot a sheer cliff of ice on the "
        "horizon. You walk towards it. When you arrive there you find a cave entrance, "
        "going deep. you also notice another entrance a short climb up. Before you can "
        "form a thought with your observations you hear something inside the caves. Climb "
        "to the higher entrance or go dead ahead.")
    stop_make_shelter_1.outputs = [
        [pins.speaker, pinState.on],
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    push_forwards_but_1 = outputNode()
    push_forwards_but_1.prompt = ("You push forwards, but find that the temperature drops along with the light, and "
        "your cloak is quickly made obsolete by the sheer cold. You try to make a shelter "
        "quickly, but its already to late and the cold sets. You collapse trying to dig "
        "out a snow bank, and you find yourself drifting off into your death. END")
    push_forwards_but_1.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    push_forwards_but_2 = outputNode()
    push_forwards_but_2.prompt = ("You push forwards, but find that the temperature drops along with the light, and "
        "your cloak is quickly made obsolete by the sheer cold. You try to make a shelter "
        "quickly, but its already to late and the cold sets. You collapse trying to dig "
        "out a snow bank, and you find yourself drifting off into your death. END")
    push_forwards_but_2.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    stop_make_shelter_2 = outputNode()
    stop_make_shelter_2.prompt = ("You stop to make a shelter, digging a small snow-fort out of the snow bank, "
        "barely large enough to fit yourself inside. You crawl in and find it plenty warm "
        "to keep you alive. You feel uncomfortable, but exhaustion makes you fall fast "
        "asleep. You awake to fresh light shining in the entrance. You crawl out and keep "
        "exploring. eventually, you spot a sheer cliff of ice on the horizon and walk "
        "towards it. When you arrive you find a cave entrance. you also notice another "
        "entrance a short climb up. Before you can form a thought you hear something "
        "inside the caves and feel a fresh gust of wind from inside. Climb to the higher "
        "entrance or go dead ahead.")
    stop_make_shelter_2.outputs = [
        [pins.fan, pinState.on],
    ]

    push_forwards_but_3 = outputNode()
    push_forwards_but_3.prompt = ("You push forwards, but find that the temperature drops along with the light, and "
        "your stone is quickly made obsolete by the sheer cold. You try to make a shelter "
        "quickly, but its already to late and the cold sets. You collapse trying to dig "
        "out a snow bank, and you find yourself drifting off into your death. END")
    push_forwards_but_3.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    hoping_might_able_1 = outputNode()
    hoping_might_able_1.prompt = ("Hoping that you might be able to avoid whatever's inside, you try to climb to "
        "the upper entrance. You get most of the way up, but your foot hold breaks off, "
        "and due to the icy nature of the cliff, the sudden force of gravity causes your "
        "hand to slip and you plummet to the ground. You die on impact. END")
    hoping_might_able_1.outputs = []

    hoping_might_able_2 = outputNode()
    hoping_might_able_2.prompt = ("Hoping that you might be able to avoid whatever's inside, you try to climb to "
        "the upper entrance. You get most of the way up, but your foot hold breaks off, "
        "and due to the icy nature of the cliff, the sudden force of gravity causes your "
        "hand to slip and you plummet to the ground. You die on impact. END")
    hoping_might_able_2.outputs = [
        [pins.speaker, pinState.on],
    ]

    walk_straight_ahead = outputNode()
    walk_straight_ahead.prompt = ("You walk straight ahead, entering the ice cave directly in front of you. You "
        "move cautiously. As you progress through, the sound you hear becomes clearer, "
        "and it sounds like the beating of massive wings. Additionally you quickly "
        "realize that the source of all the icy winds originate from here, as each step "
        "deeper into the cave is met with cutting winds so strong it threatens to knock "
        "you off balance. you eventually find a split in the path. There is a ramp up to "
        "your right, which you assume would lead you towards the higher entrance you saw "
        "earlier. To your left you see the path continues much further, and a faint glow "
        "can be seen. Go left or right.")
    walk_straight_ahead.outputs = [
        [pins.fan, pinState.on],
        [pins.speaker, pinState.on],
        [pins.cold, pinState.on],
    ]

    go_right_heading = outputNode()
    go_right_heading.prompt = ("You go right, heading up the ramp. Once you reach the top your assumptions were "
        "confirmed as you see light beaming in at the end of a long hall. Additionally, "
        "the winds seem to be stronger. In their direction, you can see the same glow as "
        "you did before. You know that nothing of note is to be found in the direction of "
        "the light, so you decide to go towards the glow. Approach the glow on your "
        "current level, or go back down and approach from there.")
    go_right_heading.outputs = []

    walk_towards_strange = outputNode()
    walk_towards_strange.prompt = ("As you walk towards the strange glow, still fighting the winds, the light gets "
        "stronger, a blood red illumination coming through the icy walls of the cave. "
        "Further you walk, and you find your destination. A large chamber, circular, with "
        "a balcony about 10 feet up that goes around the entire perimeter. Far more "
        "notable however, are 2 features. The first being a massive pentagram on the "
        "ground, from which the blood red light originates. Above that, taking up the "
        "majority of the room, is a massive figure with a muscled gray body, sharp claws "
        "as long as swords on its hands and feet, and long horns on its head. Most "
        "notable however, are the chains wrapping around the monstrosity, restraining it "
        "by holding every appendage to its body, save for massive bat like wings "
        "sprouting from its lower back, which flapped rhythmically, until the very moment "
        "you fully entered the room, when they stopped completely, along with the wind "
        "they made. The beast opens its eyes, locking onto yours, and you are filled with "
        "a dread stronger than you could have imagined. You want little more than to "
        "sprint away and never come back. Yet, in a stark contrast, you feel a pull to "
        "the center of the pentagram, just as strong as the sense of dread. Give in to "
        "the dread, or give in to the pull.")
    walk_towards_strange.outputs = []

    pushing_forward_down = outputNode()
    pushing_forward_down.prompt = ("Pushing forward, down the upper hall, still fighting the powerful gales of wind "
        "you eventually find the source of the glow in the form of a massive pentagram on "
        "the floor of an even larger circular chamber. Yet the pentagram is the lesser "
        "spectacle, as you see a massive figure with a muscled gray body, sharp claws as "
        "long as swords on its hands and feet, and long horns on its head. Most notable "
        "however, are the chains wrapping around the devil, restraining it by holding "
        "every appendage to its body, save for massive bat like wings sprouting from its "
        "lower back, which flapped rhythmically, until the very moment you fully entered "
        "the room, when they stopped completely, along with the wind. The beast is "
        "suspended from the ceiling by the chains which bind it. You stand on a balcony, "
        "10 feet up from the pentagram which circles the room, your head about at the "
        "height of its chest. The devil opens its eyes and they lock onto yours. You get "
        "filled with an intense sense of dread, and you feel a need to turn and run. "
        "Simultaneously, you feel a pull towards the center of the pentagram, just as "
        "strong as the dread. Give in to the pull, or give into the dread")
    pushing_forward_down.outputs = []

    give_sense_dread = outputNode()
    give_sense_dread.prompt = ("You give in to the sense of dread. You turn and run, back down the hall you came "
        "from, your legs moving faster than you ever had before. Behind you is the sound "
        "of thrashing chains and booming crashes against the walls. You make your way out "
        "of the cave, still sprinting, booking it across the frozen wasteland you came "
        "from. The sense of dread still grips you but you can think clearly again. Stop "
        "running or keep going.")
    give_sense_dread.outputs = [
        [pins.fan, pinState.on],
        [pins.speaker, pinState.on],
        [pins.subwoofer, pinState.on],
    ]

    keep_sprinting_pushing_1 = outputNode()
    keep_sprinting_pushing_1.prompt = ("You keep sprinting, pushing yourself to keep going. You can barely perceive the "
        "world around you as your focus is on moving as fast as you can. Keep running or "
        "stop.")
    keep_sprinting_pushing_1.outputs = [
        [pins.fan, pinState.on],
        [pins.speaker, pinState.on],
    ]

    keep_sprinting_pushing_2 = outputNode()
    keep_sprinting_pushing_2.prompt = "You keep sprinting, pushing your body close to its limit. Stop or keep going."
    keep_sprinting_pushing_2.outputs = [
        [pins.fan, pinState.on],
        [pins.speaker, pinState.on],
    ]

    still_sprinting_body = outputNode()
    still_sprinting_body.prompt = ("Still sprinting, your body reaches its limit. The sense of dread still lingers "
        "in your chest, but a sharp pain takes place beside it. You slow and and fall to "
        "your knees crawling a few more feet before rolling onto your back, "
        "hyperventilating. Unable to calm your breathing, or quell the pain in your chest "
        "you pass out, eventually succumbing to the cold as darkness falls upon your "
        "still body. You die in your sleep of hypothermia.")
    still_sprinting_body.outputs = [
        [pins.cold, pinState.on],
        [pins.fan, pinState.on],
    ]

    keep_sprinting_pushing_3 = outputNode()
    keep_sprinting_pushing_3.prompt = ("You keep sprinting, pushing your body even closer to its limit. Your lungs burn "
        "and you cant feel your legs. Stop or keep going.")
    keep_sprinting_pushing_3.outputs = [
        [pins.fan, pinState.on],
        [pins.speaker, pinState.on],
    ]

    slow_stop_falling_1 = outputNode()
    slow_stop_falling_1.prompt = ("You slow to a stop, falling on your hands and knees, your limbs going numb in "
        "the snow but you don't care as you catch your breath. You stay there panting for "
        "what feels like an eternity, but as you see the light begin to fade you come "
        "back to your senses. The dread remains in your chest, strengthening at the mere "
        "thought of going back. You make a shelter for the night, and come morning set "
        "out walking again. In your heart you know that going back is the only chance you "
        "ever have of escaping, but the sense of dread keeps you in denial, searching the "
        "frozen wastes and the scorching lower levels of this hell you find yourself in "
        "for an escape you will never find, merely surviving for the rest of your days. "
        )
    slow_stop_falling_1.outputs = []

    slow_stop_falling_2 = outputNode()
    slow_stop_falling_2.prompt = ("You slow to a stop, falling on your hands and knees and catching your breath. In "
        "moments you regain full awareness of your surroundings, but its a moment too "
        "late. The monster you saw in the chamber is free of its shackles and has "
        "clambered through the halls and made it into the wasteland. You see it flying "
        "straight towards you on shaky wings. You scramble back to your feet and start "
        "running again, but you can't move fast enough. Your lead is quickly made null "
        "and next thing you know you are in the monsters claws, torn to shreds.")
    slow_stop_falling_2.outputs = []

    give_pull_forcing = outputNode()
    give_pull_forcing.prompt = ("You give in to the pull, forcing yourself to step forward, agonizingly fighting "
        "the dread, your vision tunneling on the center of the pentagram. You move "
        "slowly, tentatively, and unthinkingly. Then, the jingling of chains and a "
        "powerful crash against the ice walls around you yanks you from your trance. You "
        "see the beast above you, thrashing in its bindings. You rush to the center of "
        "the pentagram now, inspecting it as fast as you can. You see small grooves "
        "snaking out from a reservoir in the ground. As you finish inspecting this you "
        "hear a massive snap and look up. The monster is freed from its chains and falls "
        "to the floor, standing on shaking legs as it turns to you. You notice its "
        "bleeding, presumably from the snapped chains. It moves towards you. Stand your "
        "ground or move away.")
    give_pull_forcing.outputs = [
        [pins.speaker, pinState.on],
        [pins.subwoofer, pinState.on],
    ]

    stand_ground_beast = outputNode()
    stand_ground_beast.prompt = ("You stand your ground as the beast approaches on shaky legs. It stumbles "
        "forward, its eyes locked on to you, and reaches you quickly. As it raises its "
        "gnarled claws to lash out at you, the cuts on its body from the broken chains "
        "pour blood, spattering the ground and slowly filling the reservoir. You prepare "
        "yourself to move out of the way of its slash, but the large sweep of its massive "
        "arms still catches you. The ends of its claws gash into your flesh, leaving "
        "large bloody marks on your torso and arms, and sending you spinning to the "
        "ground. You try and crawl back to your feet before it can finish you off, but it "
        "reaches out again and wraps its claws around you, dragging you back and tearing "
        "you apart. In your last moments you see the reservoir fill with a mix of you and "
        "the beasts blood. Lights start swirling above it as the grooves snaking out from "
        "the center fill. A rippling image of roiling fields begins to form beneath "
        "you...then you die. ")
    stand_ground_beast.outputs = [
        [pins.speaker, pinState.on],
    ]

    beast_approaches_shaky = outputNode()
    beast_approaches_shaky.prompt = ("As the beast approaches on shaky legs you step back, moving to the other side of "
        "the room, keeping the central reservoir between you and the monster. before long "
        "the beast crosses the gap enough to stand over the center of the room. You see "
        "its blood spatter down onto the ground, partially filling the reservoir before "
        "he crosses it completely. It is now moments from reaching you. You need to move "
        "again to stay alive. Above you you think you can reach the balcony. You could "
        "also try and move around the room to avoid the beast. Climb up or move on the "
        "ground level.")
    beast_approaches_shaky.outputs = [
        [pins.speaker, pinState.on],
    ]

    jump_grab_balcony = outputNode()
    jump_grab_balcony.prompt = ("You jump and grab the balcony, trying to pull yourself up as fast as you can. "
        "Unfortunately for you, the beast is too close behind. You get your first arm up "
        "on the platform when you feel claws pierce your lower back and drag you down. "
        "You open your mouth to scream but shock freezes your vocal cords. You slam into "
        "the ground face first. you feel your nose and jaw shatter, but you are not left "
        "to suffer for too long, as you are swiftly torn to shreds. ")
    jump_grab_balcony.outputs = [
        [pins.subwoofer, pinState.on],
    ]

    circle_around_edge = outputNode()
    circle_around_edge.prompt = ("You circle around the edge of the chamber as the devil closes in. It lashes out "
        "and you dive, narrowly avoiding it as it throws itself forward, its momentum "
        "carrying into the wall, giving you the chance to make distance. As you make it "
        "back to the center of the room you see it back on its feet, approaching once "
        "more. You notice that it seems more confident in its stride now. You sprint "
        "towards the opposite end of the room. The thought occurs to you again to climb "
        "onto the balcony. alternatively you could stay on the ground floor.")
    circle_around_edge.outputs = [
        [pins.subwoofer, pinState.on],
    ]

    make_other_end = outputNode()
    make_other_end.prompt = ("You make it to the other end of the room, and turn around to see the monster far "
        "closer behind than you thought. You try to move to avoid its claws again, but "
        "you didn't have enough distance, and the beast adapting to its newfound freedom "
        "catches you, batting you into the wall with such force that you bounced off, "
        "leaving cracks in the structure. You cant move or breath, and every bone in your "
        "body screams in pain. The last thing you see is a malicious grin on the monster "
        "open wide as it bites your head clean off.")
    make_other_end.outputs = [
        [pins.subwoofer, pinState.on],
    ]

    sprint_jump_grabbing = outputNode()
    sprint_jump_grabbing.prompt = ("You sprint and jump, grabbing onto the balcony and pulling yourself up. You feel "
        "air swipe past your feet as the devil barely misses his slash. Once on your feet "
        "you turn back to see that the central reservoir is a bit fuller. Additionally "
        "you see that the devil appears to be bleeding more heavily, likely from "
        "exertion. You need to run along the balcony. On the other side is a hallway you "
        "could escape from, or hopefully find a chance to get back down. Run left or run "
        "right.")
    sprint_jump_grabbing.outputs = [
        [pins.subwoofer, pinState.on],
    ]

    begin_sprinting_around = outputNode()
    begin_sprinting_around.prompt = ("You begin sprinting around the balcony, your eyes flashing to the devil as it "
        "cuts across the room from the lower level. In short time, it jumps and swipes, "
        "its wings flapping once as it does, and you go flying to the lower level. You "
        "cant breath, you feel warm liquid dripping down your face, and you are in "
        "extreme pain. You look back for a second to see it bearing down on you again, "
        "and you try to crawl away, desperate to survive though it feels hopeless. You "
        "find yourself directly over the reservoir when it is upon you, its talon like "
        "feet pinning you down. It's blood pours down on you and mingles with yours as it "
        "slowly opens its mouth to kill you. You start to hear a faint hum, and notice "
        "the snaking grooves in the ground filling, but pay it no mind, your focus on "
        "what your sure is to be your death. It's teeth are a centimeter away from "
        "digging into your flesh when a there is a flash of light, and you suddenly feel "
        "weightless. It only takes you a second for you to realize your falling, no "
        "longer in its grasp and watching it get farther away. Then you are submerged in "
        "water. You swim to the surface and look around. There are no monsters in sight, "
        "no barren tundra or lakes of fire. Only clear blue water and tall pine trees on "
        "the shore not far away. You swim, and stand on the beach. You feel the warm sun "
        "shine down on your aching body, soothing you with its gentle warmth. You escaped "
        "hell. ")
    begin_sprinting_around.outputs = [
        [pins.speaker, pinState.on],
        [pins.fan, pinState.on],
        [pins.heat, pinState.on],
    ]

    giving_into_pull = outputNode()
    giving_into_pull.prompt = ("Giving into the pull you stay, staring down at the center of the pentagram, "
        "noticing that there is a shallow reservoir and grooves snaking out and tracing "
        "the lines of the pentagram. You begin to crawl over the banister and lower "
        "yourself to the floor. When you land on the ground you see the devil thrashing "
        "in its chains and shortly after it falls to the ground, landing flat in the "
        "center of the room, clawing at the remaining chains on its body until its "
        "completely free. You notice its bleeding as it stands up on shaky legs and looks "
        "to you. The reservoir is partly full of its blood. It moves towards you but is "
        "slow enough for you to position it on the other side of the reservoir from you "
        "again. It makes its way towards you again, its movements more confident now. It "
        "passes over the the reservoir once more, its bleeding accelerating as it exerts "
        "itself, and blood pours in, almost filling it completely as it sprints towards "
        "you. You need to move. The thought occurs to you to climb back onto the balcony. "
        "Alternatively you could try to dodge it on the ground floor.")
    giving_into_pull.outputs = [
        [pins.speaker, pinState.on],
        [pins.subwoofer, pinState.on],
    ]

    try_avoid_devil = outputNode()
    try_avoid_devil.prompt = ("You try to avoid the devil on the ground floor, but horribly misjudge the speed "
        "of its claws. You dive, and get caught in the air, feeling claws gash your back "
        "and slam you into the floor. You don't even have time to process the pain "
        "though, as it tears you to shreds in moments, not even giving you time for a "
        "final thought. ")
    try_avoid_devil.outputs = []

    jump_up_grab = outputNode()
    jump_up_grab.prompt = ("You jump up and grab the balcony, pulling yourself up as fast as you can. You "
        "can feel the devils breath on your legs and a swish of air going past you as you "
        "just barely make it up in time. You stand and look around. You can see the "
        "entrance you came from and consider trying to escape through it. You also hope "
        "to find a chance to make your way back down to the ground level. Sprint left or "
        "right along the balcony.")
    jump_up_grab.outputs = [
        [pins.fan, pinState.on],
        [pins.subwoofer, pinState.on],
    ]

    go_through_door = outputNode()
    go_through_door.prompt = ("You go through the door as quietly as you can, breathing a sigh of relief once "
        "through, feeling confident that nothing is coming after you. You find your eyes "
        "having to adjust to the bright light. When they do you see a massive lake of "
        "fire in the distance. Moving towards it is a long path. Beside you is a rock "
        "wall with a clear top not too far up. Follow the path or climb the rock wall")
    go_through_door.outputs = [
        [pins.heat, pinState.on],
    ]


    # ── CONNECTIONS ──────────────────────────────────────────────

    beginning.add_child([["door", "open", "open door", "right"], push_open_large])
    beginning.add_child([["vent", "inspect", "inspect vent", "left"], inspect_vent_air])

    push_open_large.add_child([["left", "go left"], imp_wasnt_found])
    push_open_large.add_child([["right", "go right"], move_down_hall])

    inspect_vent_air.add_child([["door", "open", "leave", "back", "exit"], push_open_large])

    imp_wasnt_found.add_child([["door", "go through", "light", "through door"], hide_alcove_see])

    move_down_hall.add_child([["kill", "attack", "fight", "dagger", "stab"], have_dagger_lunge])
    move_down_hall.add_child([["run", "flee", "escape", "retreat", "back"], rush_back_way])

    have_dagger_lunge.add_child([["walk away", "back", "leave", "turn", "away"], walk_back_way])
    have_dagger_lunge.add_child([["door", "open", "open door"], only_open_door])

    walk_back_way.add_child([["climb", "wall", "rock", "right", "climb wall"], climb_rock_wall])

    rush_back_way.add_child([["hide", "alcove", "alcove hide"], try_hide_but])

    hide_alcove_see.add_child([["follow", "creature", "follow creature", "track"], move_down_hall])
    hide_alcove_see.add_child([["door", "go through", "light", "through door"], go_through_door])

    run_through_door.add_child([["right", "go right", "up", "climb"], run_right_find])
    run_through_door.add_child([["left", "go left"], turn_left_keep])

    climb_rock_wall.add_child([["inspect", "corpse", "body", "examine", "look"], kneeling_down_inspect_1])
    climb_rock_wall.add_child([["explore", "walk", "ignore", "start walking"], ignore_corpse_begin_1])

    walk_down_path.add_child([["right", "go right", "road", "up", "winding"], walk_up_best_2])
    walk_down_path.add_child([["left", "go left", "lake", "fire"], go_left_towards])

    run_right_find.add_child([["explore", "look around", "walk", "start"], start_explore_picking])

    turn_left_keep.add_child([["play dead", "dead", "stop", "pretend"], play_dead_hoping])

    crawl_under_overhang.add_child([["go", "walk", "continue", "forward"], walk_up_best_3])

    walk_up_best_1.add_child([["inspect", "corpse", "body", "examine"], kneeling_down_inspect_4])

    go_left_towards.add_child([["go", "walk", "continue", "forward"], walk_up_best_1])

    kneeling_down_inspect_1.add_child([["shelter", "fort", "snow fort", "stop", "build"], stop_make_shelter_1])

    kneeling_down_inspect_2.add_child([["run", "sprint", "gap", "flee", "escape"], break_into_sprint_1])

    walk_up_best_2.add_child([["inspect", "corpse", "body", "examine"], kneeling_down_inspect_3])
    walk_up_best_2.add_child([["explore", "walk", "ignore", "start"], ignore_corpse_begin_2])

    walk_up_best_3.add_child([["inspect", "corpse", "body", "examine"], kneeling_down_inspect_5])
    walk_up_best_3.add_child([["explore", "walk", "ignore", "start"], ignore_corpse_pick_2])

    kneeling_down_inspect_3.add_child([["forward", "press on", "continue", "go"], push_forwards_but_2])
    kneeling_down_inspect_3.add_child([["shelter", "stop", "fort", "build", "snow fort"], stop_make_shelter_2])

    kneeling_down_inspect_4.add_child([["shelter", "stop", "fort", "build", "snow fort"], stop_make_shelter_2])

    ignore_corpse_pick_1.add_child([["forward", "keep going", "press on", "continue"], push_forwards_but_3])
    ignore_corpse_pick_1.add_child([["shelter", "stop", "fort", "build", "snow fort"], stop_make_shelter_2])

    kneeling_down_inspect_5.add_child([["spear", "grab spear", "take", "fight", "take spear"], tear_spear_from])
    kneeling_down_inspect_5.add_child([["run", "sprint", "gap", "flee", "escape"], break_into_sprint_2])

    ignore_corpse_pick_2.add_child([["forward", "keep going", "press on", "continue"], push_forwards_but_3])

    tear_spear_out.add_child([["forward", "press on", "continue", "go"], push_forwards_but_1])
    tear_spear_out.add_child([["shelter", "stop", "fort", "build"], stop_make_shelter_1])

    tear_spear_from.add_child([["forward", "press on", "continue", "go"], push_forwards_but_3])
    tear_spear_from.add_child([["shelter", "stop", "fort", "build"], stop_make_shelter_2])

    stop_make_shelter_2.add_child([["climb", "upper", "top", "upper entrance", "go up"], hoping_might_able_2])
    stop_make_shelter_2.add_child([["straight", "ahead", "cave", "enter", "forward"], walk_straight_ahead])

    walk_straight_ahead.add_child([["glow", "light", "toward", "follow light", "go"], walk_towards_strange])

    go_right_heading.add_child([["glow", "light", "left", "go left", "toward light"], walk_towards_strange])
    go_right_heading.add_child([["forward", "right", "go right", "press on", "upper hall"], pushing_forward_down])

    walk_towards_strange.add_child([["run", "flee", "back", "retreat", "turn back"], give_sense_dread])
    walk_towards_strange.add_child([["forward", "approach", "step forward", "go", "enter"], give_pull_forcing])

    pushing_forward_down.add_child([["run", "flee", "back", "retreat", "turn back"], give_sense_dread])
    pushing_forward_down.add_child([["stay", "look", "stare", "remain", "examine"], giving_into_pull])

    give_sense_dread.add_child([["run", "keep running", "sprint", "keep going", "go"], keep_sprinting_pushing_1])
    give_sense_dread.add_child([["stop", "slow down", "rest", "catch breath", "halt"], slow_stop_falling_2])

    keep_sprinting_pushing_1.add_child([["run", "keep running", "sprint", "keep going"], keep_sprinting_pushing_2])
    keep_sprinting_pushing_1.add_child([["stop", "slow down", "rest", "halt"], slow_stop_falling_2])

    keep_sprinting_pushing_2.add_child([["stop", "slow", "rest", "halt"], slow_stop_falling_1])

    keep_sprinting_pushing_3.add_child([["run", "keep going", "sprint", "push"], still_sprinting_body])
    keep_sprinting_pushing_3.add_child([["stop", "slow", "rest", "halt"], slow_stop_falling_1])

    give_pull_forcing.add_child([["stand", "fight", "ground", "hold", "stand ground"], stand_ground_beast])
    give_pull_forcing.add_child([["back", "retreat", "step back", "move back", "away"], beast_approaches_shaky])

    beast_approaches_shaky.add_child([["jump", "balcony", "climb", "grab"], jump_grab_balcony])
    beast_approaches_shaky.add_child([["circle", "edge", "go around", "side", "around"], circle_around_edge])

    circle_around_edge.add_child([["other end", "continue", "go", "keep moving", "cross"], make_other_end])
    circle_around_edge.add_child([["jump", "sprint", "leap", "balcony", "grab"], sprint_jump_grabbing])

    sprint_jump_grabbing.add_child([["sprint", "run", "go", "move", "balcony"], begin_sprinting_around])

    giving_into_pull.add_child([["jump", "balcony", "climb", "grab", "leap"], jump_up_grab])

    jump_up_grab.add_child([["sprint", "run", "go", "move", "balcony"], begin_sprinting_around])

    go_through_door.add_child([["climb", "wall", "rock", "right", "climb wall"], climb_rock_wall])
    go_through_door.add_child([["path", "left", "go left", "ahead", "forward"], walk_down_path])
