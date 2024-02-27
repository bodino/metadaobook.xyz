import { c as create_ssr_component, e as escape, d as each, f as add_styles, h as null_to_empty, i as add_attribute } from "../../chunks/ssr.js";
const css = {
  code: ".part-button.svelte-1worm06{margin-bottom:20px;padding:10px 20px;cursor:pointer}.gallery.svelte-1worm06{display:flex;flex-wrap:wrap;justify-content:center;gap:1rem;position:relative;max-width:1600px;margin-left:auto;margin-right:auto;perspective:10000px}.image-card.svelte-1worm06{transition:transform 0.5s ease,\n            order 0.5s ease;transform-style:preserve-3d;display:flex;justify-content:center;align-items:center;margin:0.5rem}.image-card.svelte-1worm06:hover{transition:transform 0.3s ease;transform:rotateY(2deg) rotateX(2deg)}.parted.svelte-1worm06:nth-child(odd){transform:translateX(-50%) rotateY(30deg)}.parted.svelte-1worm06:nth-child(even){transform:translateX(50%) rotateY(-30deg)}.text-center.svelte-1worm06{transition:order 0.5s ease;position:absolute;top:0;left:0;width:100%;height:100%;display:flex;justify-content:center;align-items:center;pointer-events:none}img.svelte-1worm06{max-height:40rem;height:auto;width:auto;max-width:100%;display:block;backface-visibility:hidden}",
  map: null
};
const Page = create_ssr_component(($$result, $$props, $$bindings, slots) => {
  const images = Array.from({ length: 6 }).map((_, index) => `/page${index + 1}.png`);
  $$result.css.add(css);
  return `<button class="part-button svelte-1worm06">${escape("Part")}</button> <div class="gallery svelte-1worm06">${each(images, (image, index) => {
    return `<div class="${escape(null_to_empty(`image-card ${""}`), true) + " svelte-1worm06"}"${add_attribute("style", `order:${index + 1}; `, 0)}><img${add_attribute("src", image, 0)}${add_attribute("alt", `Page ${index + 1}`, 0)} draggable="false" class="svelte-1worm06"> </div>`;
  })} <div class="text-center svelte-1worm06"${add_styles({
    "order": images.length + 1
  })}>${``}</div> </div>`;
});
export {
  Page as default
};
