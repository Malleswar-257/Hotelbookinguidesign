import { useState } from 'react';
import { Search as SearchIcon, MapPin, Calendar, Users, Star, Wifi, Coffee, Dumbbell, Filter, SlidersHorizontal } from 'lucide-react';
import { ImageWithFallback } from './figma/ImageWithFallback';

interface SearchProps {
  onNavigate: (hotel: any) => void;
}

export function Search({ onNavigate }: SearchProps) {
  const [searchLocation, setSearchLocation] = useState('New York');
  const [activeFilter, setActiveFilter] = useState('All');

  const hotels = [
    {
      id: 1,
      name: 'Grand Plaza Hotel',
      location: 'Manhattan, New York',
      rating: 4.8,
      reviews: 320,
      price: 249,
      image: 'https://images.unsplash.com/photo-1590381105924-c72589b9ef3f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxsdXh1cnklMjBob3RlbCUyMGxvYmJ5fGVufDF8fHx8MTc2NTQyNDcwNXww&ixlib=rb-4.1.0&q=80&w=1080',
      amenities: ['Wifi', 'Pool', 'Gym', 'Restaurant'],
      available: 5
    },
    {
      id: 2,
      name: 'Modern City Suites',
      location: 'Brooklyn, New York',
      rating: 4.6,
      reviews: 185,
      price: 189,
      image: 'https://images.unsplash.com/photo-1572177215152-32f247303126?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxtb2Rlcm4lMjBob3RlbCUyMHJvb218ZW58MXx8fHwxNzY1NDUzMDMyfDA&ixlib=rb-4.1.0&q=80&w=1080',
      amenities: ['Wifi', 'Parking', 'Gym'],
      available: 3
    },
    {
      id: 3,
      name: 'Boutique Hotel Collection',
      location: 'SoHo, New York',
      rating: 4.9,
      reviews: 412,
      price: 329,
      image: 'https://images.unsplash.com/photo-1649731000184-7ced04998f44?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxib3V0aXF1ZSUyMGhvdGVsfGVufDF8fHx8MTc2NTQ0NDEzNHww&ixlib=rb-4.1.0&q=80&w=1080',
      amenities: ['Wifi', 'Restaurant', 'Bar', 'Spa'],
      available: 2
    },
    {
      id: 4,
      name: 'Executive Tower Hotel',
      location: 'Midtown, New York',
      rating: 4.7,
      reviews: 267,
      price: 279,
      image: 'https://images.unsplash.com/photo-1583089749897-ee5fc3d9f16b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w3Nzg4Nzd8MHwxfHNlYXJjaHwxfHxjaXR5JTIwaG90ZWwlMjBleHRlcmlvcnxlbnwxfHx8fDE3NjU1NDM5NDd8MA&ixlib=rb-4.1.0&q=80&w=1080',
      amenities: ['Wifi', 'Pool', 'Gym', 'Business Center'],
      available: 8
    },
  ];

  const filters = ['All', 'Luxury', 'Budget', 'Business', 'Boutique'];

  return (
    <div className="min-h-screen pb-12">
      {/* Search Header Banner */}
      <div 
        className="py-12 px-6"
        style={{
          background: 'linear-gradient(135deg, #BD16D6 0%, #0DDC45 100%)',
          boxShadow: '0 10px 40px rgba(189, 22, 214, 0.3)'
        }}
      >
        <div className="max-w-7xl mx-auto">
          <h1 className="text-white mb-8" style={{ textShadow: '2px 2px 4px rgba(0,0,0,0.3)' }}>
            Find Your Perfect Stay
          </h1>

          {/* Search Bar */}
          <div className="bg-white rounded-2xl p-6 shadow-2xl">
            <div className="grid md:grid-cols-4 gap-4">
              <div className="md:col-span-1">
                <label className="text-gray-600 mb-2 block">Location</label>
                <div className="relative">
                  <MapPin className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
                  <input
                    type="text"
                    value={searchLocation}
                    onChange={(e) => setSearchLocation(e.target.value)}
                    placeholder="Where to?"
                    className="w-full pl-11 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-[#BD16D6]"
                  />
                </div>
              </div>
              <div className="md:col-span-1">
                <label className="text-gray-600 mb-2 block">Check-in</label>
                <div className="relative">
                  <Calendar className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
                  <input
                    type="date"
                    className="w-full pl-11 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-[#BD16D6]"
                  />
                </div>
              </div>
              <div className="md:col-span-1">
                <label className="text-gray-600 mb-2 block">Check-out</label>
                <div className="relative">
                  <Calendar className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
                  <input
                    type="date"
                    className="w-full pl-11 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-[#BD16D6]"
                  />
                </div>
              </div>
              <div className="md:col-span-1">
                <label className="text-gray-600 mb-2 block">Guests</label>
                <div className="relative">
                  <Users className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" size={20} />
                  <select className="w-full pl-11 pr-4 py-3 border-2 border-gray-200 rounded-xl focus:outline-none focus:border-[#BD16D6] appearance-none">
                    <option>1 Guest</option>
                    <option>2 Guests</option>
                    <option>3+ Guests</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-6 py-8">
        {/* Filter Chips */}
        <div className="flex items-center gap-4 mb-8 overflow-x-auto pb-2">
          <div className="flex items-center gap-2">
            <SlidersHorizontal className="text-[#BD16D6]" size={20} />
            <span className="text-gray-700">Filters:</span>
          </div>
          {filters.map((filter) => (
            <button
              key={filter}
              onClick={() => setActiveFilter(filter)}
              className="px-6 py-2 rounded-full text-white whitespace-nowrap transition-all duration-300 hover:shadow-lg"
              style={{
                background: '#C34E49',
                opacity: activeFilter === filter ? 1 : 0.7,
                boxShadow: activeFilter === filter ? '0 5px 20px rgba(195, 78, 73, 0.4)' : 'none'
              }}
            >
              {filter}
            </button>
          ))}
        </div>

        {/* Results Header */}
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-gray-800">
            {hotels.length} hotels found in {searchLocation}
          </h2>
          <button 
            className="flex items-center gap-2 px-4 py-2 border-2 border-gray-200 rounded-xl hover:border-[#BD16D6] transition-all"
          >
            <Filter size={20} className="text-gray-600" />
            <span className="text-gray-700">More Filters</span>
          </button>
        </div>

        {/* Hotel Cards Grid */}
        <div className="grid md:grid-cols-2 gap-6">
          {hotels.map((hotel) => (
            <div
              key={hotel.id}
              onClick={() => onNavigate(hotel)}
              className="rounded-2xl overflow-hidden cursor-pointer hover:scale-[1.02] transition-all duration-300"
              style={{
                boxShadow: '0 10px 40px rgba(189, 22, 214, 0.2)',
                border: '2px solid transparent',
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.borderColor = '#BD16D6';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.borderColor = 'transparent';
              }}
            >
              {/* Hotel Image with Gradient Overlay */}
              <div className="relative h-64 overflow-hidden">
                <ImageWithFallback
                  src={hotel.image}
                  alt={hotel.name}
                  className="w-full h-full object-cover"
                />
                <div 
                  className="absolute inset-0"
                  style={{
                    background: 'linear-gradient(to top, rgba(0,0,0,0.6) 0%, transparent 50%)'
                  }}
                />
                <div className="absolute bottom-4 left-4 right-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="text-white mb-1" style={{ textShadow: '2px 2px 4px rgba(0,0,0,0.5)' }}>
                        {hotel.name}
                      </h3>
                      <div className="flex items-center gap-1 text-white opacity-90">
                        <MapPin size={14} />
                        <span style={{ textShadow: '1px 1px 2px rgba(0,0,0,0.5)' }}>{hotel.location}</span>
                      </div>
                    </div>
                    <div 
                      className="px-4 py-2 rounded-full text-white"
                      style={{ background: 'rgba(13, 220, 69, 0.9)' }}
                    >
                      {hotel.available} rooms
                    </div>
                  </div>
                </div>
              </div>

              {/* Hotel Details */}
              <div 
                className="p-6"
                style={{
                  background: 'linear-gradient(135deg, #0DDC45 0%, #C34E49 100%)',
                }}
              >
                <div className="flex items-center justify-between mb-4">
                  <div className="flex items-center gap-2">
                    <Star className="text-white fill-white" size={20} />
                    <span className="text-white">{hotel.rating}</span>
                    <span className="text-white opacity-80">({hotel.reviews} reviews)</span>
                  </div>
                  <div>
                    <span className="text-white opacity-90">From </span>
                    <span className="text-white">${hotel.price}</span>
                    <span className="text-white opacity-80">/night</span>
                  </div>
                </div>

                {/* Amenities */}
                <div className="flex flex-wrap gap-2 mb-4">
                  {hotel.amenities.map((amenity, index) => (
                    <span 
                      key={index}
                      className="px-3 py-1 rounded-full text-white text-sm"
                      style={{ background: 'rgba(255,255,255,0.2)' }}
                    >
                      {amenity}
                    </span>
                  ))}
                </div>

                {/* View Details Button */}
                <button 
                  className="w-full py-3 rounded-xl text-white transition-all duration-300 hover:shadow-xl"
                  style={{ background: '#BD16D6' }}
                >
                  View Details & Book
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
