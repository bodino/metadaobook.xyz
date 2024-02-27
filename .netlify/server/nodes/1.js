

export const index = 1;
let component_cache;
export const component = async () => component_cache ??= (await import('../entries/fallbacks/error.svelte.js')).default;
export const imports = ["_app/immutable/nodes/1.CN5JMc89.js","_app/immutable/chunks/scheduler.CKeagB7m.js","_app/immutable/chunks/index.CWajewmM.js","_app/immutable/chunks/entry.DPEfeXjh.js"];
export const stylesheets = [];
export const fonts = [];
