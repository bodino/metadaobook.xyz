export const manifest = (() => {
function __memo(fn) {
	let value;
	return () => value ??= (value = fn());
}

return {
	appDir: "_app",
	appPath: "_app",
	assets: new Set([".DS_Store","page1.png","page2.png","page3.png","page4.png","page5.png","page6.png"]),
	mimeTypes: {".png":"image/png"},
	_: {
		client: {"start":"_app/immutable/entry/start.BDPdsTSg.js","app":"_app/immutable/entry/app.C8E7xqSm.js","imports":["_app/immutable/entry/start.BDPdsTSg.js","_app/immutable/chunks/entry.DPEfeXjh.js","_app/immutable/chunks/scheduler.CKeagB7m.js","_app/immutable/entry/app.C8E7xqSm.js","_app/immutable/chunks/scheduler.CKeagB7m.js","_app/immutable/chunks/index.CWajewmM.js"],"stylesheets":[],"fonts":[],"uses_env_dynamic_public":false},
		nodes: [
			__memo(() => import('./nodes/0.js')),
			__memo(() => import('./nodes/1.js')),
			__memo(() => import('./nodes/2.js'))
		],
		routes: [
			{
				id: "/",
				pattern: /^\/$/,
				params: [],
				page: { layouts: [0,], errors: [1,], leaf: 2 },
				endpoint: null
			}
		],
		matchers: async () => {
			
			return {  };
		},
		server_assets: {}
	}
}
})();
