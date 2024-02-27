

export const index = 0;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/layout.svelte.js')).default;
export const imports = ["_app/immutable/nodes/0.NCGr8psV.js","_app/immutable/chunks/scheduler.CKeagB7m.js","_app/immutable/chunks/index.CWajewmM.js"];
export const stylesheets = [];
export const fonts = [];
