import galleryCocktails from '../IG/640408335_17874427767536399_5585709744897246926_n..jpg';
import galleryFood from '../IG/645808779_17875438455536399_6352557185933448680_n..jpg';
import galleryToast from '../IG/657975638_17879010732536399_1334222020559288473_n..jpg';
import galleryVinyl from '../IG/629902891_17873603241536399_2159782746762689174_n..jpg';

/**
 * Landing Fenomeno — traducción del export Paper→Tailwind (mar 2026).
 * Nota: el primer bloque que pegaste era Vagalume (otro archivo); este componente es solo Fenomeno.
 */
const pillars = [
  {
    title: 'Cultura del sonido',
    body: 'Vinilos, sesiones curadas y fidelidad en cada detalle de mezcla.',
  },
  {
    title: 'Fenomeno social',
    body: 'El instante donde personas, energía y espacio se alinean.',
  },
  {
    title: 'Atmósfera',
    body: 'Diseño, luz y textura para convertir cada hora en experiencia.',
  },
  {
    title: 'Mesa y barra',
    body: 'Bebidas y bocados que acompañan el ritmo de la conversación.',
  },
  {
    title: 'Puesta en escena',
    body: 'Narrativa audiovisual para que la audiencia sea parte del relato.',
  },
];

const navLinkClass =
  'font-inter uppercase tracking-[0.12em] text-[#d1cab4] text-sm transition-colors hover:text-[#e2dcc6] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#e2dcc6]';

export default function App() {
  return (
    <div className="flex min-h-screen flex-col overflow-x-hidden bg-[#131012] antialiased">
      {/* Barra superior */}
      <header className="sticky top-0 z-40 flex w-full shrink-0 justify-center border-b border-[#3a322f] bg-[#131012]/95 backdrop-blur-md">
        <div className="flex h-[4.5rem] w-full max-w-[1280px] items-center justify-between gap-4 px-5 md:px-8">
          <a
            href="#inicio"
            className="font-cormorant text-[2.5rem] italic leading-none text-[#e2dcc6] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#e2dcc6] md:text-[3.25rem]"
            aria-label="Inicio Fenomeno"
          >
            f
          </a>
          <nav aria-label="Principal" className="min-w-0">
            <ul className="flex flex-wrap items-center justify-end gap-x-4 gap-y-2 md:gap-x-8">
              <li>
                <a href="#experiencia" className={navLinkClass}>
                  Experiencia
                </a>
              </li>
              <li>
                <a href="#pilares" className={navLinkClass}>
                  Pilares
                </a>
              </li>
              <li>
                <a href="#galeria" className={navLinkClass}>
                  Galería
                </a>
              </li>
              <li>
                <a href="#visitanos" className={navLinkClass}>
                  Visítanos
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      <main id="inicio" className="flex flex-1 flex-col">
        {/* Hero: copy + collage tipo Paper */}
        <section className="flex w-full justify-center py-12 md:py-16 lg:py-20">
          <div className="flex w-full max-w-[1280px] flex-col items-stretch gap-10 px-5 md:flex-row md:items-center md:gap-14 md:px-8 lg:gap-16">
            <div className="flex min-w-0 flex-1 flex-col gap-4 md:max-w-[560px]">
              <p className="font-inter text-xs uppercase tracking-[0.14em] text-[#b9b29c]">
                Hi-Fi Bar · Madrid
              </p>
              <h1 className="font-bebas text-[clamp(4rem,15vw,8.5rem)] leading-[0.92] tracking-[0.02em] text-[#ff4b17]">
                FENOMENO
              </h1>
              <p className="font-inter text-lg leading-relaxed text-[#e2dcc6] md:text-[1.65rem] md:leading-snug">
                Sonido con carácter, coctelería precisa y una atmósfera que invita a quedarte.
              </p>
              <p className="font-inter text-base leading-relaxed text-[#b9b29c] md:text-lg md:leading-relaxed">
                Sin pretensión, con excelencia. Cada noche se dirige sola: luz justa, mezcla impecable y
                conversación viva.
              </p>
              <a
                href="#visitanos"
                className="font-inter mt-2 inline-flex h-14 w-fit min-w-[12rem] items-center justify-center rounded-full bg-[#e2dcc6] px-6 text-[15px] font-semibold text-[#131012] shadow-lg shadow-black/30 transition hover:-translate-y-0.5 hover:shadow-xl focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#e2dcc6]"
              >
                Descubrir Fenomeno
              </a>
            </div>

            <div
              className="mx-auto w-full max-w-[420px] shrink-0 overflow-hidden rounded-2xl border border-[#3a322f] bg-[#1c1718] md:max-w-[min(100%,560px)] lg:w-[min(100%,664px)]"
              aria-hidden="true"
            >
              <div className="flex border-b border-[#3a322f]">
                <div className="flex flex-[1.15] items-center justify-center bg-[#3f241d] py-4">
                  <span className="font-bebas text-[clamp(2.5rem,8vw,5.5rem)] leading-none text-[#ff4b17]">
                    FENOMENO
                  </span>
                </div>
                <div className="w-[22%] min-w-[3rem] bg-[#f4cb00]" />
                <div className="w-[20%] min-w-[2.75rem] bg-[#ff4b17]" />
              </div>
              <div className="flex border-b border-[#3a322f]">
                <div className="flex flex-1 flex-col justify-center bg-[#e2dcc6] px-4 py-4 md:px-6">
                  <p className="font-inter text-[clamp(1.25rem,4vw,2.65rem)] font-medium leading-tight text-[#2e201f]">
                    BUENOS DRINKS,
                    <br />
                    BUENA MÚSICA,
                    <br />
                    Y CERO PRISA.
                  </p>
                </div>
                <div className="hidden w-[45%] bg-[#bfb8a0] sm:block" />
              </div>
              <div className="flex">
                <div className="w-[33%] min-w-[4rem] bg-[#0f6fc1]" />
                <div className="flex flex-1 items-center justify-center bg-[#e2dcc6] py-6">
                  <p className="font-cormorant text-[clamp(2.5rem,7vw,5rem)] italic leading-none text-[#2e201f]">
                    Coming Soon
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Manifiesto */}
        <section
          id="experiencia"
          className="flex w-full justify-center border-y border-[#3a322f] py-14 md:py-16"
        >
          <div className="flex w-full max-w-[1280px] flex-col gap-6 px-5 md:flex-row md:items-start md:justify-between md:gap-16 md:px-8 lg:gap-20">
            <h2 className="font-cormorant max-w-xl text-[clamp(2rem,5vw,5.25rem)] font-medium italic leading-[1.05] text-[#e2dcc6]">
              La música se escucha de verdad.
            </h2>
            <p className="font-inter max-w-xl text-lg leading-relaxed text-[#b9b29c] md:text-2xl md:leading-relaxed">
              Fenomeno es un punto de encuentro entre cultura sonora, interiorismo y ritual social. No se trata de
              volumen ni de exceso, sino de precisión, atmósfera y estilo.
            </p>
          </div>
        </section>

        {/* Pilares */}
        <section id="pilares" className="flex w-full justify-center py-14 md:py-16">
          <div className="flex w-full max-w-[1280px] flex-col gap-5 px-5 md:px-8">
            <p className="font-inter text-xs uppercase tracking-[0.14em] text-[#b9b29c]">Pilares de contenido</p>
            <h2 className="font-cormorant text-[clamp(2rem,4vw,4.125rem)] font-medium italic leading-tight text-[#e2dcc6]">
              La noche, en cinco escenas
            </h2>
            <div className="-mx-5 flex gap-3.5 overflow-x-auto px-5 pb-2 md:mx-0 md:flex-wrap md:overflow-visible md:px-0">
              {pillars.map((p) => (
                <article
                  key={p.title}
                  className="flex w-[min(100%,280px)] shrink-0 flex-col gap-2.5 rounded-xl border border-[#3a322f] bg-[#1c1718] p-[18px] md:w-[calc(20%-12px)] md:min-w-[200px] md:flex-1"
                >
                  <h3 className="font-bebas text-[1.75rem] leading-tight text-[#e2dcc6]">{p.title}</h3>
                  <p className="font-inter text-base leading-relaxed text-[#b9b29c]">{p.body}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* Galería */}
        <section id="galeria" className="flex w-full justify-center py-14 md:py-16">
          <div className="flex w-full max-w-[1280px] flex-col gap-5 px-5 md:px-8">
            <p className="font-inter text-xs uppercase tracking-[0.14em] text-[#b9b29c]">Ambiente Fenomeno</p>
            <h2 className="font-cormorant text-[clamp(2rem,4vw,4.125rem)] font-medium italic leading-tight text-[#e2dcc6]">
              Madera, vinilos, cristal y luz
            </h2>
            <div className="flex flex-col gap-3.5">
              <div className="flex flex-col gap-3.5 md:flex-row">
                <div
                  className="relative flex min-h-[220px] flex-1 items-end rounded-xl border border-[#3a322f] p-6 md:min-h-[250px] md:flex-[1.2]"
                  style={{
                    backgroundImage:
                      'linear-gradient(145deg, oklab(32.8% 0.038 0.027) 0%, oklab(18.9% 0.009 -0.001) 100%)',
                  }}
                >
                  <img
                    src={galleryVinyl}
                    alt="Cabina con vinilos en Fenomeno"
                    className="absolute inset-0 h-full w-full rounded-xl object-cover opacity-45 mix-blend-luminosity"
                    loading="lazy"
                  />
                  <span className="font-bebas relative z-[1] text-4xl leading-none text-[#e2dcc6] md:text-5xl">
                    VINYL ROOM
                  </span>
                </div>
                <div
                  className="relative flex min-h-[220px] flex-1 items-end rounded-xl border border-[#3a322f] p-6 md:min-h-[250px]"
                  style={{
                    backgroundImage:
                      'linear-gradient(145deg, oklab(53.6% -0.048 -0.143) 0%, oklab(18.9% 0.009 -0.001) 100%)',
                  }}
                >
                  <img
                    src={galleryCocktails}
                    alt="Cocteles en la barra"
                    className="absolute inset-0 h-full w-full rounded-xl object-cover opacity-40 mix-blend-luminosity"
                    loading="lazy"
                  />
                  <span className="font-bebas relative z-[1] text-3xl leading-none text-[#e2dcc6] md:text-4xl">
                    COCKTAIL RITUAL
                  </span>
                </div>
              </div>
              <div className="flex flex-col gap-3.5 md:flex-row">
                <div className="relative min-h-[220px] flex-1 overflow-hidden rounded-xl border border-[#3a322f] md:min-h-[250px]">
                  <img
                    src={galleryFood}
                    alt="Bocados en Fenomeno"
                    className="h-full w-full object-cover"
                    loading="lazy"
                  />
                </div>
                <div className="relative min-h-[220px] flex-[1.2] overflow-hidden rounded-xl border border-[#3a322f] md:min-h-[250px]">
                  <img
                    src={galleryToast}
                    alt="Brindis en el salón"
                    className="h-full w-full object-cover"
                    loading="lazy"
                  />
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Visítanos */}
        <section
          id="visitanos"
          className="flex w-full justify-center border-t border-[#3a322f] py-14 md:py-16"
        >
          <div className="flex w-full max-w-[1280px] flex-col gap-10 px-5 md:flex-row md:justify-between md:gap-12 md:px-8">
            <div className="flex max-w-xl flex-col gap-3.5">
              <p className="font-inter text-xs uppercase tracking-[0.14em] text-[#b9b29c]">Visítanos</p>
              <h2 className="font-cormorant text-[clamp(2rem,4vw,4.125rem)] font-medium italic leading-tight text-[#e2dcc6]">
                Buenas drinks, buena música, y cero prisa.
              </h2>
              <p className="font-inter text-lg leading-relaxed text-[#b9b29c] md:text-xl md:leading-relaxed">
                Próxima apertura. Para colaboraciones, eventos privados o prensa, escribe y te respondemos con los
                detalles actualizados.
              </p>
            </div>
            <div className="flex w-full max-w-[390px] flex-col gap-3.5 rounded-2xl border border-[#3a322f] bg-[#1c1718] p-5 md:p-6">
              <p className="font-inter text-sm font-semibold text-[#e2dcc6]">Dirección</p>
              <p className="font-inter text-lg leading-relaxed text-[#d5ceb4]">
                Calle Recoletos 13
                <br />
                Salamanca, Madrid 28001
              </p>
              <p className="font-inter text-sm font-semibold text-[#e2dcc6]">Contacto</p>
              <a
                href="mailto:hola@fenomeno.bar"
                className="font-inter text-xl text-[#e2dcc6] underline-offset-2 hover:underline focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#e2dcc6]"
              >
                hola@fenomeno.bar
              </a>
              <div className="inline-flex h-8 w-fit items-center justify-center rounded-full bg-[#f4cb00] px-3">
                <span className="font-inter text-sm font-semibold text-[#131012]">Coming Soon</span>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="flex w-full justify-center border-t border-[#3a322f] py-6 md:py-7">
        <div className="flex w-full max-w-[1280px] flex-col gap-2 px-5 text-sm text-[#b9b29c] sm:flex-row sm:items-center sm:justify-between md:px-8">
          <p className="font-inter">Fenomeno · Madrid</p>
          <p className="font-inter">Instagram: @fenomeno.es</p>
        </div>
      </footer>
    </div>
  );
}
