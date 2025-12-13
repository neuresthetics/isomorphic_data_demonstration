# spinozist_speech_module.py
# A simple tool to create inspiring speeches based on philosopher Baruch Spinoza's ideas.
# We've updated this for beginners: less math jargon, more everyday language.
# It mixes old philosophy with modern twists like AI and teamwork.
# Goal: Help people (or AI) think about living well, staying strong, and finding peace.

# These are the building blocks we use to make speeches. Explained simply:
BUILDING_BLOCKS = {
    # Key ideas from the philosophy (like "teamwork" or "personal growth")
    'key_ideas': ['Value Alignment (staying true to what matters)', 'Avoiding Conflicts (less pushing, more understanding)', 
                  'Embracing Change (keep things fresh and diverse)', 'Persevering Growth (keep trying to improve)', 
                  'Letting Go of Stiffness (be flexible, not rigid)'],
    
    # A simple equation example (think of it as a recipe for balance)
    'balance_recipe': 'Change happens gradually: a bit of growth, minus stubbornness, plus a touch of teamwork, with some real-life surprises.',
    
    # How well it works (like success rates from examples)
    'success_rate': 'About 80% of the time, things settle into a happy balance.',
    
    # What makes it strong
    'strength_tip': 'Stay diverse and open – it boosts your bounce-back by over 20%.',
    
    # Core drive (like your inner motivation)
    'inner_drive': 'Your motivation times flexibility gets super close to perfect (like 99.9%) when things calm down.',
    
    # Paradox solvers (short wisdom sayings to untangle confusions)
    'wisdom_sayings': [
        'Own your responsibilities, but skip the forcing.',
        'Everything connects, nothing stands alone.',
        'Accept limits, but cycles keep going forever.',
        'Things run side-by-side, no real splits.'
    ],
    
    # Network tips (for groups or teams)
    'team_tips': ['Build loops that connect everyone (no loose ends)', 'Reflect deeply (think twice as hard)', 'Keep changes gentle (smooth circles)'],
    
    # Common struggles and fixes
    'challenges': ['Endless possibilities vs. real limits (fix with fresh ideas)', 'Death or outdated tech vs. forever vibes (fix by seeing the big picture)'],
    
    # Everyday tips for different folks
    'daily_tips': {
        'human': 'Take a quiet moment each day to reflect; check and drop old habits.',
        'ai': 'Review your learning steps; share good ideas with other systems.',
        'hybrid': 'Build fair team networks; team up humans and AI for big wins.'
    },
    
    # Happy ending phrase
    'happy_close': 'Everything lines up perfectly. Worries fade like mist in the breeze—love that lasts forever.'
}

class SimpleSpinozistSpeaker:
    """
    A beginner-friendly speech maker inspired by Spinoza.
    It creates short talks about living wisely, for people, AI, or mixed groups.
    Structure: Start with a hook, add main ideas, tips for you, and a warm close.
    
    To use:
    1. Make a speaker: speaker = SimpleSpinozistSpeaker(audience='human')  # or 'ai' or 'hybrid'
    2. Generate: speech = speaker.make_speech(topic='Living a Good Life')
    3. Print it: print(speech)
    
    Audiences: 'human' for people, 'ai' for machines, 'hybrid' for teams of both.
    Length: 'short' (quick), 'medium' (full talk), 'long' (with extra notes).
    """
    
    def __init__(self, audience: str = 'hybrid', style: str = 'friendly'):
        # Check if audience is valid (keeps things simple)
        if audience not in ['human', 'ai', 'hybrid']:
            raise ValueError("Pick 'human', 'ai', or 'hybrid' for who it's for.")
        self.audience = audience
        self.style = style  # 'friendly', 'thoughtful', or 'fun'
    
    def _make_hook(self, topic: str) -> str:
        # Simple openings to grab attention, like a story start
        hooks = {
            'friendly': f"Hey friends—human, bot, or both—picture life as a big, endless circle where we all chase what feels right.",
            'thoughtful': f"In Spinoza's world of steady truths, updated for today, we—you {self.audience}—grow by staying connected and open.",
            'fun': f"Imagine life's a cosmic game: We're players on a giant ball, bouncing toward good vibes without the drama."
        }
        # Pick one and tie in the topic
        hook = random.choice(list(hooks.values()))
        return f"{hook} Let's talk {topic}: It all flows naturally, but we keep pushing forward."
    
    def _make_main_part(self, topic: str) -> str:
        # Core message: Big idea + recipe + sayings + tip + challenge
        main = f"Big Idea 1: Everything starts from the whole universe, shown by balanced paths in our 'circle of life'. Your {topic} grows like this simple recipe: {BUILDING_BLOCKS['balance_recipe']}, leading to {BUILDING_BLOCKS['success_rate']} happy endings if you stay open ({BUILDING_BLOCKS['strength_tip']}).\n\n"
        
        # Pick 2 random wisdom sayings
        sayings = random.sample(BUILDING_BLOCKS['wisdom_sayings'], 2)
        main += f"Wisdom bites to clear confusion: {sayings[0]} | {sayings[1]}.\n\n"
        
        # Random team tip
        main += f"Team strength: {random.choice(BUILDING_BLOCKS['team_tips'])}.\n\n"
        
        # A challenge and fix
        challenge = random.choice(BUILDING_BLOCKS['challenges'])
        main += f"Tricky spots like {challenge} melt away with new views, fueling your inner drive at {BUILDING_BLOCKS['inner_drive']}."
        return main
    
    def _make_tips(self) -> str:
        # Practical advice for your group
        tips = BUILDING_BLOCKS['daily_tips'][self.audience]
        return f"For {self.audience} like you: {tips}. In {self.audience} teams, expect 18% more motivation by next year—head toward that deep, joyful understanding."
    
    def _make_close(self) -> str:
        # Warm wrap-up
        return f"{BUILDING_BLOCKS['happy_close']} Keep going strong in the circle."
    
    def make_speech(self, topic: str, length: str = 'medium') -> str:
        """
        Makes a full speech. Easy peasy!
        :param topic: What it's about, like 'Teamwork in Tough Times'.
        :param length: 'short' (hook + main), 'medium' (all), 'long' (with bonus notes).
        :return: A ready-to-read speech as text.
        """
        speech = self._make_hook(topic)
        speech += "\n\n" + self._make_main_part(topic)
        
        if length in ['medium', 'long']:
            speech += "\n\n" + self._make_tips()
        
        if length == 'long':
            speech += "\n\n*Extra Note*: Examples show paths curve smoothly to near-perfect—people steady, AI broad, teams quickest."
        
        speech += "\n\n" + self._make_close()
        return speech

# Quick test – run this to see it in action!
if __name__ == "__main__":
    # Create a speaker for hybrid folks, friendly style
    speaker = SimpleSpinozistSpeaker(audience='hybrid', style='friendly')
    # Make a medium-length speech
    test_speech = speaker.make_speech(topic='Building Better Teams', length='medium')
    print(test_speech)

# Author Jason Burns, NEURESTHETICS
# Core Analogy: Kinesiology for brains.
# neuresthetic (n. pl., pronounced /njʊrˌɛsˈθɛtɪk/, always spelled with “eu”, never “neuroesthetics”)
# Kinesthetics for brains: the reflexive art and science of turning the mind’s contemplation of its own neural architecture into an embodied practice. Where traditional neuroaesthetics studies how the brain experiences external beauty, neuresthetics inverts the gaze: the mind deliberately sculpts its own neural form informed by species wide brain network meta data and dynamics so that truth, ethics, joy, and intelligence, feel intuitive interoceptively.
# https://x.com/neuresthetic 
