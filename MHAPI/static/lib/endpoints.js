var apiUrl = 'https://serene-cove-88415.herokuapp.com';

var endpoints = {

  locations: [
    {
      route: apiUrl + '/api/locations',
      info: 'Lists all locations'
    },
    {
      route: apiUrl + '/api/locations/{location name}',
      info: 'Shows details for a specific location (i.e. /locations/Jurassic Frontier)'
    }
  ],

  weapons: [
    {
      route: apiUrl + '/api/weapons',
      info: 'Lists all weapons'
    },
    {
      route: apiUrl + '/api/weapons/{weapon name}',
      info: 'Shows single weapon details (i.e. /weapons/Petrified Blade 3)'
    }
  ],

  armor: [
    {
      route: apiUrl + '/api/armor',
      info: 'Lists all armor pieces',
    },
    {
      route: apiUrl + '/api/armor/{armor name}',
      info: 'Shows details for a single piece of armor'
    }
  ],

  monsters: [
    {
      route: apiUrl + '/api/monsters',
      info: 'Lists all monsters',
    },
    {
      route: apiUrl + '/api/monster/{monster name}',
      info: 'Shows details for a single monster'
    }
  ],

  skills: [
    {
      route: apiUrl + '/api/skills',
      info: 'Lists all skills',
    },
    {
      route: apiUrl + '/api/skills/{skill name}',
      info: 'Shows details for a single skill'
    }
  ],

  items: [
    {
      route: apiUrl + '/api/items',
      info: 'Lists all Items',
    },
    {
      route: apiUrl + '/api/items/{item name}',
      info: 'Shows details for a specific item'
    }
  ],

  crafting: [
    {
      route: apiUrl + '/api/crafting',
      info: 'Lists all crafting recipes',
    },
    {
      route: apiUrl + '/api/crafting/{recipe name}',
      info: 'Shows details for a specific crafting recipe'
    }
  ],

  quests: [
    {
      route: apiUrl + '/api/quests',
      info: 'Lists all quests',
    },
    {
      route: apiUrl + '/api/quests/{hub type - Village or Guild}/',
      info: 'Shows all quests for either Village or Guild type'
    },
    {
      route: apiUrl + '/api/quests/{hub type}/{quest name}',
      info: 'Shows details for a specific quest for either Village or Guild'
    },
    {
      route: apiUrl + '/api/quests/monsters/{monster name}',
      info: 'Shows all quests relating to a specific monster'
    },
    {
      route: apiUrl + '/api/quests/stars/{star number}',
      info: 'Shows all quests in a certain difficulty'
    }
  ]

};

